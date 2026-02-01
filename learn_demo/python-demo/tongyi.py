# langchain调用通义千问大语言模型
import os
from langchain_community.llms import Tongyi



model = Tongyi(model="qwen-max", api_key=os.getenv("DASHSCOPE_API_KEY"))

res = model.invoke(input="你是谁能做什么？") 

print(res)