from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(
  file_path="./data/1.pdf",
  mode="single", # 默认的page模式，每个页面形成一个document文档对象；single模式，将所有页面的文本内容合并到一个document文档对象中；
  password=None, # pdf文件如果加密了，需要在此处输入密码才可以读取
)

i = 0 
for doc in loader.lazy_load():
  i += 1
  print(i, doc)
