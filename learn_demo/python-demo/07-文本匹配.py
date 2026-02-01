import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

example_data = {
    "是": [
        ("公司ABC发布了季度财报,显示盈利增长", "财务披露,公司ABC利润上升"),
        ("新产品发布会吸引了大量关注", "市场活动,公司XYZ推出新产品"),
        ("公司DEF宣布与公司GHI达成战略合作", "合作伙伴关系,公司DEF与公司GHI合作"),
    ],
    "不是": [
        ("黄金价格下降,投资者抛售", "外汇市场交易额创新高"),
        ("央行降息以刺激经济", "新能源技术的创新"),
    ],
}

questions = [
    ("公司ABC发布了季度财报,显示盈利增长", "财务披露,公司ABC利润上升"),
    ("新产品发布会吸引了大量关注", "市场活动,公司XYZ推出新产品"),
    ("公司DEF宣布与公司GHI达成战略合作", "合作伙伴关系,公司DEF与公司GHI合作"),
    ("黄金价格下降,投资者抛售", "外汇市场交易额创新高"),
    ("央行降息以刺激经济", "新能源技术的创新"),
]

"""
[
  {"role": "system", "content": f"你帮我完成文本匹配,我给你2个句子,你判断它是否匹配,回答是或不是,请参照如下示例"},
  
  {"role": "user", "content": "句子1:[公司ABC发布了季度财报,显示盈利增长]。句子2:[财务披露,公司ABC利润上升。]"},
  {"role":"assistant", "content": "是"},
  
  {"role": "user", "content": "句子1:[新产品发布会 attracted a lot of attention]。句子2:[市场活动,公司XYZ推出新产品。]"},
  {"role":"assistant", "content": "是"},
  
  {"role": "user", "content": "句子1:[公司DEF宣布与公司GHI达成战略合作]。句子2:[合作伙伴关系,公司DEF与公司GHI合作。]"},
  {"role":"assistant", "content": "是"},
  
  {"role": "user", "content": "句子1:[黄金价格下降,投资者抛售]。句子2:[外汇市场交易额创新高。]"},
  {"role":"assistant", "content": "不是"},
  
  {"role": "user", "content": "句子1:[央行降息以刺激经济]。句子2:[新能源技术的创新。]"},
  {"role":"assistant", "content": "不是"},
  
  {"role": "user", "content": f"按照上述示例,现在判断这两个句子是否匹配:句子1:[{要匹配的句子1}]。句子2:[{要匹配的句子2}]"},
  
]
"""

messages = [
    {
        "role": "system",
        "content": f"你帮我完成文本匹配,我给你2个句子,你判断它是否匹配,回答是或不是,请参照如下示例",
    },
]

for key, value in example_data.items():
    for t in value:
        messages.append({"role": "user", "content": f"句子1:[{t[0]}]。句子2:[{t[1]}]"})
        messages.append({"role": "assistant", "content": key})

for q in questions:
    response = client.chat.completions.create(
        model="qwen3-max",
        messages=messages
        + [{"role": "user", "content": f"句子1:[{q[0]}],句子2:[{q[1]}]"}],
    )
    print(response.choices[0].message.content)
