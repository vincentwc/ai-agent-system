import os
from langchain_community.llms.tongyi import Tongyi
from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate.from_template("你是一个AI助手")

model = Tongyi(model="qwen-max", api_key=os.getenv("DASHSCOPE_API_KEY"))

chain = prompt | model


# <class 'langchain_core.runnables.base.RunnableSequence'>
print(type(chain))

