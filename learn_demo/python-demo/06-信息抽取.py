import json
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

schema = ["日期", "股票名称", "开盘价", "收盘价", "成交量"]

example_data = [
    {
        "content": "2023-01-10,股市震荡,股票强大科技A股今日开盘100人名币,一度飙升至105人名币,随后回落至98人名币收盘,成交量达到520000.",
        "answer": {
            "日期": "2023-01-10",
            "股票名称": "强大科技A股",
            "开盘价": "100人名币",
            "收盘价": "98人名币",
            "成交量": "520000",
        },
    },
    {
        "content": "2023-01-11,股市震荡,股票英伟达今日开盘200美元,一度飙升至210美元,随后回落至190美元收盘,成交量达到5120000.",
        "answer": {
            "日期": "2023-01-11",
            "股票名称": "英伟达",
            "开盘价": "200美元",
            "收盘价": "190美元",
            "成交量": "5120000",
        },
    },
]

questions = [
    "2025-06-16,股市利好,股票传智教育A股今日开盘52人名币,一度飙升至55人名币,随后回落至48人名币收盘,成交量达到12500.",
    "2025-06-17,股市利好,股票黑马今日开盘200人名币,一度飙升至210人名币,随后回落至190人名币收盘",
]

"""
[
  {"role": "system", "content": f"帮我完成信息抽取,我给你句子,你抽取{schema}信息,按json字符串输出,如果某些信息不存在,用‘原文未提及’表示,请参照如下示例"},
  
  {"role": "user", "content": "2023-01-10,股市震荡,股票强科技A股今日开盘100人名币,一度飙升至105人名币,随后回落至98人名币收盘,成交量达到520000."}
  {"role": "assistant", "content": '{"日期": "2023-01-10", "股票名称": "强科技A股", "开盘价": "100人名币", "收盘价": "98人名币", "成交量": "520000"}'},
  
  {"role": "user", "content": "2023-01-11,股市震荡,股票英伟达今日开盘200美元,一度飙升至210美元,随后回落至190美元收盘,成交量达到5120000."},
  {"role": "assistant", "content": '{"日期": "2023-01-11", "股票名称": "英伟达", "开盘价": "200美元", "收盘价": "190美元", "成交量": "5120000"}'},
  
  {"role": "user", "content": f"按照上述示例,现在抽取这个句子的信息：{要抽取的句子文本}"},
]
"""

messages = [
    {
        "role": "system",
        "content": f"帮我完成信息抽取,我给你句子,你抽取{schema}信息,按json字符串输出,如果某些信息不存在,用‘原文未提及’表示,请参照如下示例",
    },
]

for example in example_data:
    messages.append({"role": "user", "content": example["content"]})
    messages.append(
        {
            "role": "assistant",
            "content": json.dumps(example["answer"], ensure_ascii=False),
        }
    )

for q in questions:
  response = client.chat.completions.create(
    model="qwen3-max",
    messages=messages+[{"role": "user", "content": f"按照上述的示例,现在抽取这个句子信息：{q}"}],
  )
  print(response.choices[0].message.content)
