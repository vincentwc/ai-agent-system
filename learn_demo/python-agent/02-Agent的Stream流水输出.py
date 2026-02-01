from langchain.agents import create_agent
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.tools import tool


@tool("get_price", description="获取股价,传入股票名称,返回股票价格信息")
def get_price(name: str) -> str:
    """
    获取指定股票的价格
    :param name: 股票名称
    :return: 股票价格字符串
    """
    return f"股票{name}的价格是100元"


@tool("get_info", description="获取指定股票的信息,传入股票名称,返回股票相关信息")
def get_info(name: str) -> str:
    """
    获取指定股票的信息
    :param name: 股票名称
    :return: 股票信息字符串
    """
    return f"股票{name},是一家A股上市公司,专注IT职业教育"


# 创建一个基于Tongyi模型的智能体
agent = create_agent(
    model=ChatTongyi(model="qwen3-max"),
    tools=[get_price, get_info],  # 工具函数列表
    system_prompt="你是一个智能助手，可以回答股票相关问题，记住请告知我思考过程，让我知道你为什么调用某个工具。",  # 系统提示
)

for chunk in agent.stream(
    {
        "messages": [
            {
                "role": "user",
                "content": "传智教育股价多少，并介绍一下?",
            }
        ]
    },
    stream_mode="values",
):
    print(chunk)
    # latest_messages = chunk["messages"][-1]

    # if latest_messages.content:  #
    #     print(type(latest_messages).__name__, latest_messages.content)
    # try:
    #   if latest_messages.tool_calls:  # 工具调用
    #       print(f"工具调用:{[tc['name'] for tc in latest_messages.tool_calls]}")
    # except AttributeError as e:
    #     pass
