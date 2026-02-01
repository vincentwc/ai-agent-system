from langchain_core.prompts import (
    PromptTemplate,
    FewShotPromptTemplate,
    ChatPromptTemplate,
)

"""
PromptTemplate -> StringPromptTemplate
FewShotPromptTemplate -> StringPromptTemplate
ChatPromptTemplate -> BaseChatPromptTemplate
"""


template = PromptTemplate.from_template("我的领居是:{lastname},最喜欢：{hobby}")

res = template.format(lastname="张三", hobby="打篮球")  # 我的领居是:张三,最喜欢：打篮球

print(res, type(res)) # string


res2= template.invoke({"lastname": "张三", "hobby": "打篮球"})

print(res2, type(res2))  # PromptValue

