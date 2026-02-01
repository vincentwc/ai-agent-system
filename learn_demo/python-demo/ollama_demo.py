# langchain调用ollama大语言模型
from langchain_ollama import OllamaLLM

model = OllamaLLM(model="qwen3:4b")

res = model.invoke(input="What is the meaning of life?")

print(res)