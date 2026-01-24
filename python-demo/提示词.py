from openai import OpenAI

import os


# 1. 获取client对象
client = OpenAI(
    # api_key=os.getenv("DASHSCOPE_API_KEY"),
    # base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    base_url="http://localhost:11434/v1",
)

example_data = {
    "新闻报道": "今日股市大涨，科技板块表现尤为突出，投资者信心回升。",
    "财务报告": "公司2023年第一季度收入同比增长20%，净利润达到5000万元。",
    "公司公告": "公司将于下周一召开股东大会，讨论年度分红方案。",
    "分析师报告": "分析师预计未来六个月内，科技行业将继续保持强劲增长势头。",
}

# 分类列表
example_types = ["新闻报道", "财务报告", "公司公告", "分析师报告"]

# 提问问题
questions = [
    "今日，央行发布公告，宣布将下调存款准备金率，以刺激经济增长。",
    "本季度，公司实现营业收入1亿元，同比增长15%，净利润800万元。",
    "公司宣布将于下月启动新产品发布会，届时将展示最新技术成果。",
    "分析师指出，随着5G技术的普及，相关产业链有望迎来爆发式增长。",
    "aaaaaaaa",
]

"""
[
  {"role": "system", "content": "你是金融专家，将文本分类为['新闻报道', '财务报告', '公司公告', '分析师报告'],不清楚的分类为'不清楚类型'，以下事例"},
  {"role": "user", "content": "今日，央行发布公告，宣布将下调......"},
  {"role":"assistant", "content": "新闻报道"},
  {"role": "user", "content": "本季度，公司实现营业收入1亿元
  {"role":"assistant", "content": "财务报告"},
  {"role": "user", "content": "公司宣布将于下月启动新产品发布会......"},
  {"role":"assistant", "content": "公司公告"},
  {"role": "user", "content": "分析师指出，随着5G技术的普及......"},
  {"role":"assistant", "content": "分析师报告"}
  
  {"role": "user", "content": "要提问的问题"},
]
"""

messages = [
    {
        "role": "system",
        "content": "你是金融专家，将文本分类为['新闻报道', '财务报告', '公司公告', '分析师报告'],不清楚的分类为'不清楚类型'",
    },
]

for key, value in example_data.items():
    messages.append({"role": "user", "content": value})
    messages.append({"role": "assistant", "content": key})

# 向模型提问
for q in questions:
    response = client.chat.completions.create(
        model="qwen3:4b",
        messages=messages
        + [{"role": "user", "content": f"按照事例，回答这段文本的分类列别：{q}"}],
    )
    print(response.choices[0].message.content)
