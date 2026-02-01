from langchain.agents import create_agent
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.tools import tool


@tool("get_weather")
def get_weather(location: str) -> str:
    """
    获取指定位置的天气信息
    :param location: 位置名称
    :return: 天气描述字符串
    """ 
    return "天气晴朗"


agent = create_agent(
    model=ChatTongyi(model="qwen3-max"),
    tools=[get_weather],  # 工具函数列表
    system_prompt="你是一个聊天助手，能够回答客户问题。",  # 系统提示
)

res = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "明天武汉的天气如何?",
            }
        ]
    }
)

# print(res)

for msg in res["messages"]:
    print(type(msg).__name__, msg.content)
