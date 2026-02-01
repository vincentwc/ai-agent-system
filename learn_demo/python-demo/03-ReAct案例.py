
from langchain.agents import create_agent
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.tools import tool


@tool("get_weight", description="获取体重,返回数是整数,单位是kg")
def get_weight() -> int:
    """
    获取体重
    """
    return 100


@tool("get_height", description="获取身高,返回数是整数,单位是cm")
def get_height() -> int:
    """
    获取身高
    """
    return 170


# 创建一个基于Tongyi模型的智能体
agent = create_agent(
    model=ChatTongyi(model="qwen3-max"),
    tools=[get_weight, get_height],  # 工具函数列表
    system_prompt="""
      你是严格遵守ReAct框架的智能体，必须按照以下格式进行思考和执行：
      1. 思考：根据用户问题，思考需要调用哪些工具以及工具的参数。
      2. 调用工具：根据思考结果，调用相应的工具函数。
      3. 执行：根据工具函数的返回值，执行后续操作。
      4. 回答：根据执行结果，回答用户问题。
      5. 每一轮仅调用一个工具函数，不能同时调用多个工具函数。
      并告知我你的思考过程，工具的调用原因，按思考、行动、观察三个结构告知我
    """,  # 系统提示
)

for chunk in agent.stream(
    {
        "messages": [
            {
                "role": "user",
                "content": "计算我的bmi指数?",
            }
        ]
    },
    stream_mode="values",
):
    # print(chunk)
    latest_messages = chunk["messages"][-1]

    if latest_messages.content:  #
        print(type(latest_messages).__name__, latest_messages.content)
    try:
      if latest_messages.tool_calls:  # 工具调用
          print(f"工具调用:{[tc['name'] for tc in latest_messages.tool_calls]}")
    except AttributeError:
        pass
