from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = TextLoader(file_path="./data/python基础语法.txt", encoding="utf-8")

docs = loader.load()

spliter = RecursiveCharacterTextSplitter(
    chunk_size=500,  # 分段最大字符数
    chunk_overlap=50,  # 分段之间允许重叠字符数
    # 文本自然段落分隔的依据符号
    separators=["\n\n", "\n", "(?<=\. )", " ", "", ",", ".", "?", "，", "。", "？"],
    length_function=len,
)

split_docs = spliter.split_documents(docs)
print(len(split_docs))

for doc in split_docs:
  print("="*20)
  print(doc.page_content)
  print("="*20)