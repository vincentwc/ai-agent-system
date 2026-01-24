import os
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.messages import AIMessage

parser = StrOutputParser()

model = ChatTongyi(model="qwen-max", api_key=os.getenv("DASHSCOPE_API_KEY"))

prompt = PromptTemplate.from_template(
    "我的领居姓：{lastname},刚生了{gender}，请帮我起一个名字"
)

chain = prompt | model | parser | model | parser

res = chain.invoke({"lastname": "张", "gender": "儿子"})

print(res)
