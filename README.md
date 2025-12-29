



## 环境准备

### 1、安装Anaconda

- 创建名称为ai的虚拟环境

  ```bash
  # 创建【python版本不需要最新，选择最稳定的版本】
  conda create -n ai python=3.10.19
  
  # 使用
  conda activate ai
  ```
  
- 安装依赖

  ```bash
  # 激活环境（确保已激活）
  conda activate ai
  
  # 安装基础包
  pip install requests python-dotenv httpx  # httpx 是 LangChain 推荐的异步客户端
  ```
  
  

## 项目目录

​	项目命名 **`ai-agent-system`**，并有清晰的架构意识——**多语言协同（Java + Python）+ 模块化演进**。这是构建生产级 AI 智能体系统的正确思路。

### 🧱 1、整体架构定位

> **`ai-agent-system` 是一个“智能体中枢系统”**，核心目标是：
>
> - 对外提供统一智能服务（问答、工具调用、决策）
> - 对内整合 Python（AI 能力） + Java（业务集成）
> - 支持未来扩展（前端、移动端、插件等）

### 📂 2、推荐项目目录结构

```bash
ai-agent-system/
├── docs/                     # 系统设计文档、API 文档、学习笔记
├── deployments/              # Docker Compose、K8s 配置、部署脚本
├── libs/                     # 共享工具库（如 proto 定义、公共 DTO）
│
├── python-agent/             # 👉 核心 AI 智能体（Python）
│   ├── core/                 # LangChain/AutoGen 逻辑
│   ├── api/                  # FastAPI 接口层
│   ├── cli/                  # 命令行工具
│   ├── web/                  # Gradio/Streamlit Demo
│   └── tests/
│
├── java-client/              # 👉 Java 调用端（Spring Boot Starter 或 SDK）
│   ├── src/main/java/com/yourcompany/aiagent/
│   │   ├── client/           # WebClient 封装
│   │   ├── dto/              # 请求/响应 DTO（与 Python API 对齐）
│   │   └── config/           # 自动配置（@Configuration）
│   └── src/test/
│
├── frontend/                 # （可选）管理后台或用户界面（React/Vue）
├── plugins/                  # （未来）自定义工具插件（如企业微信、钉钉）
│
├── .gitignore
├── README.md                 # 项目总览 + 快速启动指南
└── LICENSE
```

### 🔍 3、各模块职责详解

| 模块               | 技术栈                                        | 职责                                                         | 关键产出                                          |
| ------------------ | --------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------- |
| **`python-agent`** | Python 3.10+, LangChain, FastAPI, Chroma      | 实现智能体核心能力： - RAG - 工具调用 - 多智能体协作 - 记忆管理 | REST API (`/ask`, `/chat`)、CLI 工具、Web Demo    |
| **`java-client`**  | Java 17+, Spring Boot 3.x, WebClient, Jackson | 作为业务系统的“智能代理”： - 封装 HTTP 调用 - 处理重试/熔断 - 转换 JSON ↔ Java 对象 | `AIAgentService` Bean，支持 `@Autowired` 直接使用 |
| **`libs/`**        | Protocol Buffers / OpenAPI / Shared DTO       | 定义 **跨语言契约**： - 请求/响应结构 - 错误码规范           | `ai_agent.proto` 或 `openapi.yaml`                |
| **`deployments/`** | Docker, docker-compose.yml                    | 一键启动整个系统： - Python API 服务 - 向量数据库 - （可选）Redis | `docker-compose up` 即可运行                      |

### ➕4、初始化仓库

```bash
# 在项目根目录创建文件夹
mkdir -p docs deployments libs python-agent java-client
```



## 第一周

### 1、安装依赖

```bash
cd ai-agent-system/python-agent
conda activate ai

# 安装本周所需包（全部兼容 Python 3.10）
pip install \
  requests==2.31.0 \
  python-dotenv==1.0.1 \
  fastapi==0.115.0 \
  "uvicorn[standard]==0.32.0" \
  httpx==0.27.0
  
# 说明：uvicorn需要加""的原因是，mac的zsh客户端会把[standard] 当作通配符（类似正则）
```

### 2、创建标准目录结构

```bash
mkdir -p src/{agent,cli,api}
touch src/__init__.py
```

### 3、最终目录结构

```bash
python-agent/
├── .env                 ← 你手动创建（含 API Key）
├── README.md
├── requirements.txt     ← 建议生成（见下文）
└── src/
    ├── __init__.py
    ├── agent/
    │   └── core.py
    ├── cli/
    │   └── weather_cli.py
    └── api/
        └── main.py
```

```bash
# 运行以下命令记录依赖
pip freeze > requirements.txt
```



## Dify

https://docs.dify.ai/zh/self-host/quick-start/docker-compose
