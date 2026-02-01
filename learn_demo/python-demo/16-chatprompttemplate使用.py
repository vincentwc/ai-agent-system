import os
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_models.tongyi import ChatTongyi

chat_prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个边塞诗人，可以做诗"),
        MessagesPlaceholder("history"),
        ("human", "请再来一首唐诗"),
    ]
)


history_data = [
    ("human", "请帮我写一首唐诗"),
    ("ai", "春眠不觉晓，处处闻啼鸟。夜来风雨声，花落知多少。"),
    ("human", "好诗，请再来一首唐诗"),
    ("ai", "白日依山尽，黄河入海流。欲穷千里目，更上一层楼。"),
]

res = chat_prompt_template.invoke({"history": history_data}).to_string()

# print(res)

model = ChatTongyi(model="qwen3-max", api_key=os.getenv("DASHSCOPE_API_KEY"))

response = model.invoke(res)

print(response.content, type(response))
