import os
from langchain_core.prompts import PromptTemplate
from langchain_community.llms.tongyi import Tongyi



prompt_template = PromptTemplate.from_template("我的领居姓{lastname},他的名字叫{firstname}。")


prompt_text = prompt_template.format(lastname="张", firstname="三")
# '我的领居姓张,他的名字叫三。'

print(prompt_text)

model = Tongyi(model="qwen-max", api_key=os.getenv("DASHSCOPE_API_KEY"))

# res= model.invoke(prompt_text)

# print(res)

# 链式. lcel表达式
chain = prompt_template | model

res = chain.invoke(input = {"lastname": "张", "firstname": "三"})

print(res)