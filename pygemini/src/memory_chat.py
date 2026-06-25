import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

os.environ["http_proxy"] = "http://127.0.0.1:7890"
os.environ["https_proxy"] = "http://127.0.0.1:7890"

load_dotenv()

# =====================================================================
# 1. 优化提示词：明确命令模型必须基于历史事实回答，不能盲目脑补
# =====================================================================
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "你是一名正在打 CS 的硬核玩家队友。说话简短、专业。"
        "【铁律】你必须严格根据 `chat_history` 中队友提过的历史经济和战术事实来回答问题，绝对不能凭空编造过去的回合经历。"
    ),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}")
])

# =====================================================================
# 2. 降低温度值：从 0.7 降到 0.2，让模型变得更严谨、更注重事实
# =====================================================================
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.2)

chain = prompt | llm

session_store = {}


def get_session_history(session_id: str):
    if session_id not in session_store:
        session_store[session_id] = InMemoryChatMessageHistory()
    return session_store[session_id]


agent_with_memory = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="chat_history",
)

# =====================================================================
# 3. 运行测试：为了看清本质，我们顺便把底层的历史记录打印出来看看
# =====================================================================
session_config = {"configurable": {"session_id": "dust2_match_02"}}

print("--- 回合 1 ---")
response1 = agent_with_memory.invoke(
    {"input": "这局我们经济不好，全体 ECO (经济局)，我发了一把 P250。"},
    config=session_config
)
print(f"队友回复: {response1.content}")

print("\n--- 调试：当前内存中的历史记录 ---")
current_history = get_session_history("dust2_match_02")
print(current_history.messages)
print("-" * 30)

print("\n--- 回合 2 ---")
response2 = agent_with_memory.invoke(
    {"input": "A大有脚步声，准备回防！对了，上一局我们的经济策略是什么来着？"},
    config=session_config
)
print(f"队友回复: {response2.content}")
