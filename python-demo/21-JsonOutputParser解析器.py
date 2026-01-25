from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import PromptTemplate

# 创建所需的解析器
str_parser = StrOutputParser()
json_parser = JsonOutputParser()

# 模型初始化
model = ChatTongyi(model="qwen3-max")

# 定义第一个提示模板
first_prompt = PromptTemplate.from_template(
    "我的领居姓：{lastname},刚生了{gender},请帮我起一个名字,并封装成json格式返回给我，要求key是name，value是名字，请严格遵守格式要求"
)

# 定义第二个提示模板
second_prompt = PromptTemplate.from_template("姓名：{name},请帮我解释含义")


# 创建链条
chain = first_prompt | model | json_parser | second_prompt | model | str_parser

#  invoke 调用
# res = chain.invoke({"lastname": "李", "gender": "男孩"})


# print(res)
# print(type(res))

#  stream流式输出
for chunk in chain.stream({"lastname": "张", "gender": "儿子"}):
    print(
        chunk,
        end="",
        flush=True,
    )
