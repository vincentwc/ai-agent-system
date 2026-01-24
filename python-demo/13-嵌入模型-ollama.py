import os
from langchain_ollama.embeddings import OllamaEmbeddings


# 初始化嵌入模型对象，默认使用的模型是 text-embedding-v1
embed = OllamaEmbeddings(model="qwen3-embedding:4b")

# 测试---单次转换
print(embed.embed_query("我喜欢你"))

# 测试---批量转换
# print(embed.embed_documents(["我喜欢你", "我不喜欢你","我稀饭你","xxx"]))