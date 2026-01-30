md5_path = "./md5.txt"

# Chroma向量库配置
chroma_collection_name = "rag"
embedding_model = "text-embedding-v4"
chroma_persist_directory = "./chroma_db"

# splitter配置
separators = ["\n\n", "\n", ".", "!", "?"]
chunk_size = 1000
chunk_overlap = 100
max_split_char_number=1000 # 文本分隔的阈值

operator = "vincent" # 操作人名称
