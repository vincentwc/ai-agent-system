md5_path = "./md5.txt"

# 模型配置
embedding_model = "text-embedding-v4"
chat_model = "qwen3-max"

# Chroma向量库配置
chroma_collection_name = "rag"
chroma_persist_directory = "./chroma_db"
similarity_threshold = 1 # 相似度阈值,默认1

# splitter配置
separators = ["\n\n", "\n", ".", "!", "?"]
chunk_size = 1000
chunk_overlap = 100
max_split_char_number=1000 # 文本分隔的阈值

operator = "vincent" # 操作人名称

