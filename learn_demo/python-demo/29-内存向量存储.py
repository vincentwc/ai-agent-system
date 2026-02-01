from langchain_core.vectorstores import InMemoryVectorStore
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.document_loaders import CSVLoader

vector_store = InMemoryVectorStore(
    embedding=DashScopeEmbeddings(),
)

loader = CSVLoader(
    file_path="./data/info.csv",
    encoding="utf-8",
    source_column="source",  # 指定本条数据的来源是哪里
)

documents = loader.load()
# print(documents[1])

# 向量存储的 新增 删除 检索
vector_store.add_documents(
    documents=documents,  # 被添加的文档 list[document]
    ids=["id" + str(i) for i in range(1, len(documents) + 1)],  # 给添加的文档提供id
)

vector_store.delete(["id1", "id2"])

result = vector_store.similarity_search("python学起来简单吗？", 3)

print(result)
