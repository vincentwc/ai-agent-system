from typing import Callable
from utils.prompt_loader import load_system_prompts, load_report_prompts
from langchain.agents import AgentState
from langchain.agents.middleware import (
    wrap_tool_call,
    before_model,
    dynamic_prompt,
    ModelRequest,
)
from langchain.tools.tool_node import ToolCallRequest
from langchain_core.messages import ToolMessage
from langgraph.runtime import Runtime
from langgraph.types import Command
from utils.logger_handler import logger


@wrap_tool_call()
def monitor_tool(
    request: ToolCallRequest,
    handler: Callable[[ToolCallRequest], ToolMessage | Command],
):
    """
    监控工具执行的调用
    :param request: 工具调用请求数据封装
    :param handler: 工具调用处理函数
    :return: 工具调用结果
    """
    logger.info(
        f"[monitor_tool]执行工具: {request.tool_call['name']}，参数: {request.tool_call['args']}"
    )
    try:
        result = handler(request)
        logger.info(f"[monitor_tool]工具 {request.tool_call['name']} 调用成功")
        return result
    except Exception as e:
        logger.error(
            f"[monitor_tool]工具 {request.tool_call['name']} 调用异常,原因: {str(e)}"
        )
        raise e


@before_model
def log_before_model(
    state: AgentState,
    run: Runtime,
):
    """
    模型调用前日志记录
    :param state: 整个agent智能体中的状态记录
    :param run: 记录了整个执行过程中的上下文信息
    """

    logger.info(f"[log_before_model]模型调用前:带有 {len(state['messages'])} 条消息")

    logger.debug(
        f"[log_before_model]{type(state['messages'][-1]).__name__} | {state['messages'][-1].content.strip()}"
    )  # 打印最新一条消息的内容
    
    return None
  

