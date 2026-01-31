from vector_stores import VectorStoreService
from langchain_community.embeddings import DashScopeEmbeddings
import config_data as config
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import MessagesPlaceholder
from langchain_community.chat_models import ChatTongyi
from langchain_core.runnables import (
    RunnableLambda,
    RunnablePassthrough,
    RunnableWithMessageHistory,
)
from langchain_core.documents import Document
from langchain_core.output_parsers import StrOutputParser
from file_history_store import get_history


def print_prompt(prompt):
    print("=" * 20)
    print(prompt.to_string())
    print("=" * 20)
    return prompt


class RagService(object):
    def __init__(self, embedding):
        self.vector_service = VectorStoreService(
            embedding=DashScopeEmbeddings(model=config.embedding_model)
        )
        self.prompt_template = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "以我提供的已知参考资料为主,简介和专业的回答用户问题。参考资料:{context}.",
                ),
                ("system", "并且我提供用户的对话历史记录如下:"),
                MessagesPlaceholder(variable_name="history"),
                ("human", "请回答用户问题:{input}"),
            ]
        )
        self.chat_model = ChatTongyi(model=config.chat_model)
        self.chain = self.__get_chain()

    def __get_chain(self):
        """
        获取最终执行的链链
        """
        retrievers = self.vector_service.get_retriever()

        def format_document(docs: list[Document]):
            if not docs:
                return "无相关参考资料"
            format_str = ""

            for doc in docs:
                format_str += f"文档片段:{doc.page_content}\n:文档元数据:{doc.metadata}"
            return format_str

        def format_for_retriever(value):
            return value["input"]

        def format_for_template(value):
            # print("----", value)
            # {input, context, history}
            new_value = {
                "input": value["input"]["input"],
                "context": value["context"],
                "history": value["input"]["history"],
            }
            return new_value

        chain = (
            {
                "input": RunnablePassthrough(),
                "context": RunnableLambda(format_for_retriever)
                | retrievers
                | format_document,
            }
            | RunnableLambda(format_for_template)
            | self.prompt_template
            | print_prompt
            | self.chat_model
            | StrOutputParser()
        )

        conversation_chain = RunnableWithMessageHistory(  # 历史记忆的链
            chain,
            get_history,
            input_messages_key="input",
            history_messages_key="history",
        )

        return conversation_chain


if __name__ == "__main__":
    # session_id配置
    session_config = {"configurable": {"session_id": "user_001"}}
    rag_service = RagService(
        embedding=DashScopeEmbeddings(model=config.embedding_model)
    )
    res = rag_service.chain.invoke({"input": "羽绒服如何保养？"}, session_config)
    print(res)
