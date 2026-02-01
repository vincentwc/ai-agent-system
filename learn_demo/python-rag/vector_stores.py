from langchain_chroma import Chroma
import config_data as config


class VectorStoreService(object):
    def __init__(self, embedding) -> None:
        """
        初始化向量存储服务
        params:
          embedding: 嵌入模型的传入实例
        """
        self.embedding = embedding

        self.vector_store = Chroma(
            collection_name=config.chroma_collection_name,
            embedding_function=self.embedding,
            persist_directory=config.chroma_persist_directory,
        )
        
    def get_retriever(self):
      """
      获取向量存储的检索器,方便加入链中使用
      """
      return self.vector_store.as_retriever(search_kwargs={"k": config.similarity_threshold})


# if __name__ == "__main__":
#     from langchain_community.embeddings import DashScopeEmbeddings
#     service = VectorStoreService(DashScopeEmbeddings(model=config.embedding_model))
#     retriever = service.get_retriever()
#     res = retriever.invoke("我的体重180斤,尺码推荐")
#     print(res)
