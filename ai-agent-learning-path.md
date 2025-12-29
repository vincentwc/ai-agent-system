# 🧠 AI智能体应用开发12周学习路线  
## —— 专为 Java 程序员设计的转型路径  

> **目标**：从零构建端到端 AI 智能体系统，并实现与 Java 后端无缝集成  
> **核心栈**：Python + LangChain / LlamaIndex / AutoGen + FastAPI + Docker + Spring Boot  
> **成果输出**：GitHub 作品集 + 可演示智能体系统 + Java 调用客户端  

---

## ✅ 学习原则

- **每周聚焦一个能力模块**，循序渐进
- **动手优先**：每周末交付可运行代码/文档
- **工程化思维**：包含测试、日志、部署、可观测性
- **Java 友好**：第8周起无缝对接 Spring Boot，前期铺垫 Python 基础

---

## 📅 详细周计划

### 🔹 第 1 周：环境搭建 & 智能体初体验

**学习重点**：
- 安装 Python 3.10+、pip、virtualenv
- 注册通义千问（Qwen）或 OpenAI API Key
- 体验 Dify（低代码智能体平台）
- 编写第一个 CLI 智能体（调用大模型 API）

**增强建议**：
- 快速掌握 Python 基础语法（对比 Java）
- 使用 `.env` 管理敏感密钥
- 理解 prompt、completion、function calling 概念

**交付物**：
- `weather_cli.py`：支持自然语言查天气（调用和风天气 API 或 mock）
- Dify 智能体链接 + 截图说明
- `README.md`：记录环境配置步骤

---

### 🔹 第 2 周：Python 进阶 & LangChain 入门

**学习重点**：
- Python 类、函数、列表推导、requests 库
- Pydantic 数据模型（用于工具输入校验）
- LangChain 核心概念：LLM、PromptTemplate、Tool、AgentExecutor

**增强建议**：
- 用 `@tool` 装饰器定义工具
- 对比 Dify 与手写 LangChain 的控制粒度

**交付物**：
- `weather_agent_langchain.py`：基于 LangChain 的天气助手
- 对比笔记：Dify vs LangChain（控制流、调试难度、扩展性）

---

### 🔹 第 3 周：RAG 基础（检索增强生成）

**学习重点**：
- 文档加载（PDF、TXT、Markdown）
- 文本切片策略（固定长度 vs 语义分块）
- Embedding 模型（如 `bge-small-zh` 或 `text-embedding-ada-002`）
- 向量数据库（Chroma / FAISS）

**增强建议**：
- 使用真实技术文档（如公司制度 PDF）
- 测试不同 Embedding 模型效果

**交付物**：
- `rag_qa.py`：支持上传文档并问答
- 准确率测试表（5个问题 vs 人工答案）

---

### 🔹 第 4 周：RAG Web 化 & 优化

**学习重点**：
- Gradio 快速构建 Web UI
- 显示引用来源（高亮原文片段）
- 优化切片策略（重叠、滑动窗口）

**增强建议**：
- 部署到 Hugging Face Spaces（免费）
- 添加“清空对话”按钮

**交付物**：
- 可运行 RAG Web 应用（本地或在线）
- 切片策略对比报告（段落 vs 句子 vs 语义分块）

---

### 🔹 第 5 周：记忆机制（多轮对话）

**学习重点**：
- LangChain 内存类型：`ConversationBufferMemory`、`SummaryMemory`
- 控制 token 消耗
- Redis 作为持久化存储（可选）

**增强建议**：
- 先实现简单内存，再尝试摘要压缩
- 测试上下文丢失场景

**交付物**：
- `memory_customer_agent.py`：支持记住用户姓名、偏好
- 多轮对话测试记录（如：“我叫李四” → “好的，李四先生…”）

---

### 🔹 第 6 周：工具扩展 & 错误处理

**学习重点**：
- 自定义多个工具（查日历、发邮件模拟、计算等）
- 工具输入校验（Pydantic）
- 异常捕获与重试（`tenacity` 库）

**增强建议**：
- 模拟工具失败场景（如网络超时）
- 实现 fallback 逻辑（如“无法发送邮件，请稍后重试”）

**交付物**：
- 多工具智能体脚本
- 日志文件（含错误回退记录）

---

### 🔹 第 7 周：API 化 & Docker 部署

**学习重点**：
- FastAPI 构建 REST API（自动生成 Swagger）
- 请求/响应模型（Pydantic）
- 编写 Dockerfile 并容器化

**增强建议**：
- 多阶段构建减小镜像体积
- 使用 `gunicorn` 提升并发

**交付物**：
- `main.py`（FastAPI 接口）
- `Dockerfile`
- `curl` 调用示例（如 `curl -X POST http://localhost:8000/ask -d '{"query":"你好"}'`）
- 可选：部署到 Render / 阿里云 ECS

---

### 🔹 第 8 周：Java 集成（关键里程碑）

**学习重点**：
- Spring Boot 创建 HTTP 客户端
- 使用 `WebClient`（响应式）或 `RestTemplate`
- JSON 反序列化（Jackson + DTO）
- 错误码统一处理

**增强建议**：
- **提前准备**：第1周就创建 `ai-agent-java-client` 项目骨架
- 添加熔断机制（Resilience4j）
- 支持异步调用

**交付物**：
- `AIServiceClient.java`
- 端到端测试：Java → Python API → 返回结构化结果（如 `{"answer": "...", "sources": [...]}`）
- 单元测试（Mock Server）

---

### 🔹 第 9 周：多智能体协作（AutoGen）

**学习重点**：
- Microsoft AutoGen 框架
- 定义角色：Planner、Writer、Reviewer
- 组织群聊（GroupChat）

**增强建议**：
- 限制最大对话轮次（防死循环）
- 输出结构化结果（如 Markdown 周报）

**交付物**：
- `multi_agent_team.py`
- 自动生成的周报样例（含任务分解、内容撰写、校对）

---

### 🔹 第 10 周：性能与成本优化

**学习重点**：
- 缓存机制（`functools.lru_cache` 或 Redis）
- 流式响应（FastAPI `StreamingResponse`）
- Token 统计与模型选择（Qwen-Max vs Qwen-Plus）

**增强建议**：
- 记录每次调用的 token 消耗
- 设置 token 上限防止失控

**交付物**：
- 优化后的 API 服务
- 成本日志（如：平均每次请求消耗 800 tokens）

---

### 🔹 第 11 周：测试 & 可观测性

**学习重点**：
- 单元测试（mock LLM 调用）
- 结构化日志（JSON 格式）
- Prometheus 指标（可选）

**增强建议**：
- 使用 `pytest` + `responses` 库
- 日志包含 trace_id 便于追踪

**交付物**：
- `test_agent.py`
- `logging_config.py`
- README.md 更新：含测试、部署、监控说明

---

### 🔹 第 12 周：项目整合 & 演示

**学习重点**：
- 统一入口：根据用户意图路由到 RAG / 工具 / 多智能体
- 支持多种交互方式：CLI、Web、API
- 编写完整文档

**增强建议**：
- 设计一个综合场景（如“企业知识助手”）
- 录制 2 分钟演示视频

**交付物**：
- 完整智能体系统（含 `/cli`, `/web`, `/api` 目录）
- GitHub 仓库（含清晰 README、目录结构、Java 调用示例）
- 演示视频（Loom / Bilibili 链接）
- 简历可引用的项目描述（STAR 法则）

---

## 🧰 推荐工具与资源

| 类别 | 推荐 |
|------|------|
| **大模型** | 通义千问 Qwen（阿里）、DeepSeek、Moonshot（国产友好） |
| **框架** | LangChain、LlamaIndex、AutoGen、FastAPI |
| **向量库** | Chroma（轻量）、FAISS（高效）、Milvus（生产级） |
| **部署** | Docker、Render、Hugging Face Spaces、阿里云 ECS |
| **Java 集成** | Spring Boot + WebClient + Jackson |
| **学习资料** | [LangChain 中文文档](https://www.langchain.com.cn/)、[Qwen 技术博客](https://help.aliyun.com/zh/qwen) |

---

## 💡 给 Java 程序员的特别提示

1. **Python 不必精通**：只需掌握读写能力，重点在逻辑而非语法
2. **智能体核心在 Python**：生态成熟，Java 作为调用方更高效
3. **作品集 > 证书**：12 周后你将拥有 3–5 个可展示项目
4. **拥抱国产生态**：Qwen + 百炼 + Dify 在国内部署更顺畅

---

## 🚀 下一步行动

- ✅ 将本文保存为 `ai-agent-learning-path.md`
- ✅ 创建 GitHub 仓库：`yourname/ai-agent-system`
- ✅ 第1天：安装 Python + 创建虚拟环境 + 跑通第一个 API 调用

---

> **记住**：AI 工程师的核心能力不是调参，而是**把智能体可靠地集成到业务系统中**。你已具备最强的工程底座——Java 开发经验，现在只需补齐 AI 应用层拼图！

祝你转型顺利！如有需要，我可继续提供：
- Python 速成对照表（Java → Python）
- 每周任务清单（Excel / Notion 模板）
- 第12周 Demo 场景设计（如“HR 智能助手”）

## 📒项目目录信息

```
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

