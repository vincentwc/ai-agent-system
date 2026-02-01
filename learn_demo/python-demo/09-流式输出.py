# from langchain_community.llms import Tongyi
# import os

# model = Tongyi(model="qwen-max", api_key=os.getenv("DASHSCOPE_API_KEY"))

# # 通过stream获取流式输出

# res = model.stream(input="请介绍一下你自己，并且每隔一秒输出一句话，共输出五句话。")

# for chunk in res:
#     print(chunk, end="", flush=True)


import os
from langchain_ollama import OllamaLLM

model = OllamaLLM(model="qwen3:4b", api_key=os.getenv("DASHSCOPE_API_KEY"))

res = model.stream(input="请介绍一下你自己，并且每隔一秒输出一句话，共输出五句话。")

for chunk in res:
    print(chunk, end="", flush=True)