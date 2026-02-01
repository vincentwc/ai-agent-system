from langchain.agents import AgentState, create_agent
from langchain.agents.middleware.types import (
    before_agent,
    after_agent,
    before_model,
    after_model,
    wrap_model_call,
    wrap_tool_call,
)
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.tools import tool
from langgraph.runtime import Runtime


@tool(
    "get_weather", description="获取指定城市的天气信息,传入城市名称,返回天气描述字符串"
)
def get_weather(city: str) -> str:
    """
    获取指定城市的天气信息
    :param city: 城市名称
    :return: 天气描述字符串
    """
    return "天气晴朗"


"""
1. agent执行前
2. agent执行后
3. model执行前
4. model执行后
5. 工具执行中
6. 模型执行中
"""


@before_agent
def before_agent_hook(state: AgentState, runtime: Runtime) -> None:
    """
    agent执行前钩子函数
    :param state: 智能体状态
    :param runtime: 运行时实例
    :return: None
    """
    # print(f"agent执行前: {state['messages']}")
    print(f"[before agent]agent启动,并附带{len(state['messages'])}条消息")


@after_agent
def after_agent_hook(state: AgentState, runtime: Runtime) -> None:
    """
    agent执行后钩子函数
    :param state: 智能体状态
    :param runtime: 运行时实例
    :return: None
    """
    # print(f"agent执行后: {state['messages']}")
    print(f"[after agent]agent执行完毕,并附带{len(state['messages'])}条消息")


@before_model
def before_model_hook(state: AgentState, runtime: Runtime) -> None:
    """
    model执行前钩子函数
    :param state: 智能体状态
    :param runtime: 运行时实例
    :return: None
    """
    # print(f"model执行前: {state['messages']}")
    print(f"[before model]model即将调用,并附带{len(state['messages'])}条消息")


@after_model
def after_model_hook(state: AgentState, runtime: Runtime) -> None:
    """
    model执行后钩子函数
    :param state: 智能体状态
    :param runtime: 运行时实例
    :return: None
    """
    # print(f"model执行后: {state['messages']}")
    print(f"[after model]model执行完毕,并附带{len(state['messages'])}条消息")


@wrap_model_call
def wrap_model_call_hook(request, handler):
    """
    model调用中钩子函数
    :param request: 模型调用请求
    :param handler: 模型调用处理函数
    :return: ModelResponse
    """
    print(f"[wrap model call]模型调用了,请求参数为{request}")
    return handler(request)


@wrap_tool_call
def wrap_tool_call_hook(request, handler):
    """
    工具调用中钩子函数
    :param request: 工具调用请求
    :param handler: 工具调用处理函数
    :return: ToolResponse
    """
    print(
        f"[wrap tool call]工具调用:{request.tool_call['name']},参数为{request.tool_call['args']}"
    )
    return handler(request)


agent = create_agent(
    model=ChatTongyi(model="qwen3-max"),
    tools=[get_weather],  # 工具函数列表
    middleware=[
        before_agent_hook,
        after_agent_hook,
        before_model_hook,
        after_model_hook,
        wrap_model_call_hook,
        wrap_tool_call_hook,
    ],
    # system_prompt="""
    #   你是严格遵守ReAct框架的智能体，必须按照以下格式进行思考和执行：
    #   1. 思考：根据用户问题，思考需要调用哪些工具以及工具的参数。
    #   2. 调用工具：根据思考结果，调用相应的工具函数。
    #   3. 执行：根据工具函数的返回值，执行后续操作。
    #   4. 回答：根据执行结果，回答用户问题。
    #   5. 每一轮仅调用一个工具函数，不能同时调用多个工具函数。
    #   并告知我你的思考过程，工具的调用原因，按思考、行动、观察三个结构告知我
    # """,  # 系统提示
)

res = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "今天武汉的天气如何?",
            }
        ]
    }
)

print("*********\n", res)
