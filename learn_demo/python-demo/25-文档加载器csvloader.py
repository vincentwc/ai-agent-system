from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(
    file_path="./data/stu.csv",
    csv_args={
        "delimiter": ",",  # 指定分隔符
        "quotechar": '"',  # 指定带有分隔符文本的引号包围是单引号还是双引号
        # "fieldnames": ["name", "age", "sex", "score"], 指定表头。如果数据有表头，则不需要指定表头
    },
    # encoding="utf-8",  # 指定编码
)

# # load 批量获取数据
# documents = loader.load()

# for document in documents:
#     print(document)


# lazy_load 获取数据懒加载
for document in loader.lazy_load():
    print(document)
