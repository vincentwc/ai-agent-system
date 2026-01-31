from vector_stores import VectorStoreService
from langchain_community.embeddings import DashScopeEmbeddings
import config_data as config
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatTongyi
from langchain_core.runnables import RunnablePassthrough
from langchain_core.documents import Document
from langchain_core.output_parsers import StrOutputParser

def print_prompt(prompt):
    print("="*20)
    print(prompt.to_string())
    print("="*20)
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

        chain = {
            "input": RunnablePassthrough(),
            "context": retrievers | format_document,
        } | self.prompt_template | print_prompt | self.chat_model  | StrOutputParser()
        return chain


if __name__ == "__main__":
    rag_service = RagService(
        embedding=DashScopeEmbeddings(model=config.embedding_model)
    )
    res = rag_service.chain.invoke("我的体重180斤,尺码推荐")
    print(res)
