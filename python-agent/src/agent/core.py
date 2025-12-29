# -*- coding: utf-8 -*-
import os
import requests
from dotenv import load_dotenv


# 加载.env文件
load_dotenv()

# 从环境变量中获取配置
DASHSCOPE_API_KEY = os.getenv("DASHSCOPE_API_KEY")
DEFAULT_MODEL = os.getenv("QWEN_MODEL", "qwen-max")

if not DASHSCOPE_API_KEY:
    raise EnvironmentError(
        "DASHSCOPE_API_KEY is not set in environment variables.\n"
        "Please set it in .env file or environment variables."
    )


def call_qwen_api(prompt: str, model: str = DEFAULT_MODEL) -> str:
    """
    调用通义千问API接口
    :param prompt: 用户输入的提示语
    :param model: 使用的模型名称
    :return: 模型生成的文本响应
    """
    url = (
        "https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation"
    )
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {DASHSCOPE_API_KEY}",
    }
    payload = {
        "model": model,
        "input": {"messages": [{"role": "user", "content": prompt}]},
        "messages": [{"role": "user", "content": prompt}],
        # "parameters": {
        #     "temperature": 0.7,
        #     "top_p": 0.8,
        # },
    }

    response = requests.post(url, json=payload, headers=headers, timeout=30)
    if response.status_code == 200:
        return response.json()["output"]["text"]
    else:
        f"Error: {response.status_code}, {response.text}"


def get_weather(location: str) -> str:
    """
    获取指定位置的天气信息
    :param location: 位置名称
    :return: 天气描述字符串
    """
    return f"当前{location}天气晴朗，气温25°C。"


def main():
    user_input = input("请输入您的问题(例如：北京的天气如何？）")

    if "天气" in user_input:
        location = (
            user_input.replace("天气", "").replace("如何", "").replace("？", "").strip()
        )
        weather_info = get_weather(location)
        prompt = f"请用自然友好的语气回答：{weather_info}"
        answer = call_qwen_api(prompt)
        print("🤖:", answer)
    else:
        # 直接交给大模型
        print("🤖:", call_qwen_api(user_input))


if __name__ == "__main__":
    main()
