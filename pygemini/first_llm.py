import os

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()
# 初始化 Gemini 模型对象
# 我们使用 gemini-pro 模型，并设置 temperature（数值越高，回答越具创造力和随机性）
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)

# response = llm.invoke("向第一次学习Langchain的开发者说一句鼓励的话吧！")
# 1.定义模板
promt =PromptTemplate.from_template("请用{style}的语气，向我介绍一下{topic}。")

# 2.组装链 创建一个最简单的“链”(Chain)
# 这里的 | 符号把 prompt 和 llm 连接了起来
chain = promt|llm

# 3.运行这个链 通过字典传入具体的变量值
response = chain.invoke({
    "style": "幽默且通俗移动",
    "topic": "什么是大语言模型 LLM"
})

print(response.content)
