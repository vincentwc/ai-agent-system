"""
基于streamlit完成web网页上传服务

streamlit run app_file_uploader.py
"""

import streamlit as st

# 添加网页标题
st.title("知识库更新服务")

# file_uploader
uploader_file = st.file_uploader(
    "请上传TXT|JSON文件",
    type=["txt","json"],
    accept_multiple_files=False,  # 不接受多个文件上传
)

if uploader_file is not None:
    # 提取文件信息
    file_name = uploader_file.name
    file_type = uploader_file.type
    file_size = uploader_file.size / 1024  # 转换为KB

    st.subheader("文件信息")
    st.write(f"文件名: {file_name}")
    st.write(f"格式: {file_type}｜大小: {file_size:.2f}KB")
    
    # get_value -> byte -> decode('utf-8')
    text = uploader_file.getvalue().decode('utf-8')
    st.write(f"文件内容: {text}")
    
