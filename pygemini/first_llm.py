import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()
# 2. 初始化 Gemini 模型对象
# 我们使用 gemini-pro 模型，并设置 temperature（数值越高，回答越具创造力和随机性）
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)

response = llm.invoke("向第一次学习Langchain的开发者说一句鼓励的话吧！")

print(response.content)
