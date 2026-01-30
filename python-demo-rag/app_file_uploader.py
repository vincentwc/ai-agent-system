"""
基于streamlit完成web网页上传服务

pip install streamlit

streamlit run app_file_uploader.py

streamlit:当WEB页面元素发生变化,会触发页面重新渲染
"""

import streamlit as st
import time
from knowledge_base import KnowledgeBaseService

# 添加网页标题
st.title("知识库更新服务")

# file_uploader
uploader_file = st.file_uploader(
    "请上传TXT|JSON文件",
    type=["txt", "json"],
    accept_multiple_files=False,  # 不接受多个文件上传
)


# session_state 中存储 KnowledgeBaseService 实例
if "service" not in st.session_state:
    st.session_state["service"] = KnowledgeBaseService()

if uploader_file is not None:
    # 提取文件信息
    file_name = uploader_file.name
    file_type = uploader_file.type
    file_size = uploader_file.size / 1024  # 转换为KB

    st.subheader(f"文件名: {file_name}")
    st.write(f"格式: {file_type}｜大小: {file_size:.2f}KB")

    # get_value -> byte -> decode('utf-8')
    text = uploader_file.getvalue().decode("utf-8")

    with st.spinner("载入知识库中..."): # 模拟耗时操作,会有一个转圈效果
        time.sleep(1) # 模拟耗时操作,1秒
        result = st.session_state["service"].upload_by_str(text, file_name)
        st.write(result)
