from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import (
    PromptTemplate,
    ChatPromptTemplate,
    MessagesPlaceholder,
)
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory

model = ChatTongyi(model="qwen3-max")

# prompt = PromptTemplate.from_template(
#     "你需要根据会话历史回应用户问题。对话历史：{chat_history},用户提问:{input}, 请回答"
# )

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "你需要根据会话历史回应用户问题。"),
        MessagesPlaceholder("chat_history"),
        ("human", "请回答如下问题：{input}"),
    ]
)

str_parser = StrOutputParser()


def print_prompt(full_prompt):
    print("模型输入：", full_prompt.to_string())
    return full_prompt


base_chain = prompt | print_prompt | model | str_parser

store = {}  # key:会话id, value:InMemoryChatMessageHistory类对象


# 实现通过会话id获取InMemoryChatMessageHistory类对象
def get_history(session_id: str) -> InMemoryChatMessageHistory:
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory(session_id=session_id)
    return store[session_id]


# 创建一个新的链，对原有链增强功能，自动附加历史消息
conversation_chain = RunnableWithMessageHistory(
    base_chain,  # 被增强对原有链
    get_history,  # 通过绘会话id获取InMemoryChatMessageHistory类对象
    input_messages_key="input",  # 表示用户输入在模版中的占位符
    history_messages_key="chat_history",  # 表示用户输入在模版中的占位符
)


if __name__ == "__main__":
    # 固定格式，添加langchain的配置，为当前程序配置所属的session_id
    session_config = {"configurable": {"session_id": "user_001"}}
    res = conversation_chain.invoke({"input": "小明有两个猫"}, session_config)
    print("第一次执行" + res)

    res = conversation_chain.invoke({"input": "小刚有两只猫"}, session_config)
    print("第二次执行" + res)

    res = conversation_chain.invoke({"input": "总共有几只宠物"}, session_config)
    print("第三次执行" + res)
