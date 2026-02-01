from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
import os



model = ChatOllama(model="qwen3:4b", base_url="http://localhost:11434/v1")

messages = [
  SystemMessage(content="你是一个边塞诗人"),
  HumanMessage(content="写一首唐诗"),
  AIMessage(content="锄禾日当午，汗滴禾下土。谁知盘中餐，粒粒皆辛苦。"),
  HumanMessage(content="按照你上一个回复的格式，在写一首唐诗")
]



res = model.stream(input=messages)

for chunk in res:
    print(chunk.content,end="", flush=True)