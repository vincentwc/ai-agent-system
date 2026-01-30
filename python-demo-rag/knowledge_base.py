"""
知识库管理服务
"""

import os
import config_data as config
import hashlib
from langchain_chroma import Chroma
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from datetime import datetime


def check_md5(md5_str: str) -> bool:
    """
    检查文件MD5是否已存在于知识库中
    return False(md5未处理过) True(已处理过,已有记录)
    """
    if not os.path.exists(config.md5_path):
        # 文件不存在,则直接返回False
        open(
            config.md5_path,
            "w",
            encoding="utf-8",  # w：写入模式,如果文件不存在则创建,如果文件存在则覆盖（会清空文件内容）
        ).close()  # 当文件不存在时,创建空文件
        return False
    else:
        # 文件存在,则检查是否已存在该MD5值
        for line in open(config.md5_path, "r", encoding="utf-8").readlines():
            line = line.strip()  # 移除行尾的换行符
            if line == md5_str:
                return True  # 已存在该MD5值,则返回True
        return False


def save_md5(md5_str: str) -> None:
    """
    保存文件MD5字符,记录到文件内保存
    """
    with open(config.md5_path, "a", encoding="utf-8") as f:  # a：追加模式
        f.write(md5_str + "\n")  # 写入MD5值,并添加换行符


def get_string_md5(input_str: str) -> str:
    """
    计算字符串的MD5值
    """
    # 将字符串转换为字节流数组bytes,并计算MD5值
    md5_hash = hashlib.md5()  # 创建MD5哈希对象
    md5_hash.update(
        input_str.encode("utf-8")
    )  # 更新哈希对象的状态,将字符串转换为字节流数组bytes
    return md5_hash.hexdigest()  # 返回MD5值的十六进制字符串表示


class KnowledgeBaseService(object):
    def __init__(self) -> None:
        # 创建向量库存储目录,如果不存在则创建
        os.makedirs(config.chroma_persist_directory, exist_ok=True)
        self.chroma = Chroma(  # 向量存储实例 Chroma向量库对象
            collection_name=config.chroma_collection_name,  # 向量库名称
            embedding_function=DashScopeEmbeddings(model=config.embedding_model),
            persist_directory=config.chroma_persist_directory,  # 向量库存储目录
        )
        self.spliter = RecursiveCharacterTextSplitter(  # 文本分割器对象
            separators=config.separators,  # 分隔符列表,按顺序尝试分割文本
            chunk_size=config.chunk_size,  # 每个分块的最大字符数
            chunk_overlap=config.chunk_overlap,  # 相邻分块之间的重叠字符数
            length_function=len,  # 用于计算分块长度的函数,这里使Python的内建len函数
        )

    def upload_by_str(self, data: str, filename: str):
        """
        将传入的字符串进行向量化,存入到向量数据库中
        """
        md5_hex = get_string_md5(data)  # 计算字符串的MD5值
        if check_md5(md5_hex):  # 检查MD5值是否已存在
            return "[跳过]内容已存在知识库中"  # 如果已存在,则直接返回,不进行重复处理
        if (
            len(data) > config.max_split_char_number
        ):  # 如果字符串长度超过阈值,则进行分块
            knowladge_chunks: list[str] = self.spliter.split_text(data)
        else:
            knowladge_chunks: list[str] = [data]

        metadata = {
            "source": filename,  # 为每个分块添加元数据,source字段记录文件名
            "create_time": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),  # 为每个分块添加元数据,create_time字段记录创建时间
            "operator": config.operator,  # 为每个分块添加元数据,operator字段记录操作人
        }
        # 对字符串进行向量化,并存储到向量数据库中
        self.chroma.add_texts(
            texts=knowladge_chunks,  # 文本分块列表
            metadatas=[metadata for _ in knowladge_chunks],
            # 为每个分块添加元数据,source字段记录文件名
        )
        
        # 保存MD5值,记录到文件内保存
        save_md5(md5_hex)
        return "[成功]内容已存入知识库"


if __name__ == "__main__":
    service = KnowledgeBaseService()
    r= service.upload_by_str("这是一个测试字符串22", "testfile")
    print(r)
