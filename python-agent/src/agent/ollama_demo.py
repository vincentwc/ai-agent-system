from langchain_ollama import ChatOllama

model = ChatOllama(
    model="qwen3:4b",
    validate_model_on_init=True,
    temperature=0.8,
    num_predict=256,
    base_url="http://127.0.0.1:11434",
    # other params ...
)