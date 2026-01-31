import streamlit as st
import time
from rag import RagService
import config_data as config
from langchain_community.embeddings import DashScopeEmbeddings

# 标题
st.title("智能客服")
st.divider()  # 分隔线


if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "你好，有什么可以帮助你？"}
    ]

if "rag" not in st.session_state:
    st.session_state["rag"] = RagService(
        embedding=DashScopeEmbeddings(model=config.embedding_model)
    )

# 显示历史消息
for message in st.session_state["messages"]:
    role = message["role"]
    avatar = "🧑‍💻" if role == "user" else "🤖"
    st.chat_message(role, avatar=avatar).write(message["content"])

# 用户输入框
# user_input = st.text_input("请输入您的问题：")
prompt = st.chat_input()

if prompt:
    # 在页面输出用户的提问
    st.chat_message("user", avatar="🧑‍💻").write(prompt)

    st.session_state["messages"].append({"role": "user", "content": prompt})

    ai_res_list = []
    with st.spinner("AI思考中..."):
        res_stream = st.session_state["rag"].chain.stream(
            {"input": prompt}, config.session_config
        )
        
        def capture(generator,cache_list):
          for chunk in generator:
            cache_list.append(chunk)
            yield chunk
        
        
        # 在页面输出客服的回答
        st.chat_message("assistant", avatar="🤖").write(capture(res_stream,ai_res_list))
        # 缓存客服的回答
        st.session_state["messages"].append({"role": "assistant", "content": "".join(ai_res_list)})
