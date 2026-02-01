from langchain_community.document_loaders import JSONLoader

#  json文件
# loader = JSONLoader(
#   file_path="./data/stu.json", 
#   jq_schema=".", #
#   text_content=False, # 告知jsonloader，抽取的内容不是字符串
# )


# document = loader.load()
# print(document)

#  json数组
# loader = JSONLoader(
#   file_path="./data/stus.json", 
#   jq_schema=".[].name", #
#   text_content=False, # 告知jsonloader，抽取的内容不是字符串
# )

# document = loader.load()
# print(document)

# json行
loader = JSONLoader(
  file_path="./data/stu_json_lines.json", 
  jq_schema=".name", #
  text_content=False, # 
  json_lines=True, # 告知jsonloader，是json行格式
)

document = loader.load()
print(document)