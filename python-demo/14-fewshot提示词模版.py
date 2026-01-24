import os
from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate
from langchain_community.llms.tongyi import Tongyi

# 示例模版
example_prompt = PromptTemplate.from_template("单词：{word},反义词：{antonym}")

# 示例数据
example_data = [
    {"word": "高兴", "antonym": "难过"},
    {"word": "快速", "antonym": "缓慢"},
    {"word": "强", "antonym": "弱"},
]


few_shot_template = FewShotPromptTemplate(
    example_prompt=example_prompt,  # 示例模板
    examples=example_data,  # 示例数据
    prefix="告知我单词的反义词，我提供如下的示例：",  # 前缀提示词
    suffix="基于前面的示例告知我,{input_word}的反义词是？",  # 后缀提示词
    input_variables=["input_word"],  # 申明在前缀或后缀中所需要注入的变量名
)

prompt_text = few_shot_template.invoke(input={"input_word": "聪明"}).to_string()

# print(prompt_text)

model = Tongyi(model="qwen-max", api_key=os.getenv("DASHSCOPE_API_KEY"))

print(model.invoke(prompt_text))