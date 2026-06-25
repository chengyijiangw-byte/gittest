from typing import List

from dotenv import load_dotenv
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, Field

load_dotenv()


# =====================================================================
# 1. 定义数据结构 (Schema)
# 使用 Pydantic 定义我们期望大模型返回的标准结构。Field 的 description 极其重要，
# 因为 LangChain 会把这些描述作为提示词的一部分喂给大模型，指导它如何填空。
# =====================================================================
class TechStackReview(BaseModel):
    language: str = Field(description="编程语言或框架的名称")
    advantages: List[str] = Field(description="该技术的三个核心核心优势列表")
    difficulty_level: str = Field(description="学习难度，只能是 '简单'、'中等' 或 '困难' 之一")


# =====================================================================
# 2. 初始化输出解析器
# =====================================================================
parser = PydanticOutputParser(pydantic_object=TechStackReview)

# =====================================================================
# 3. 编写提示词模板
# 这里的 {format_instructions} 是一个特殊的占位符，LangChain 会自动在里面
# 注入一段告诉大模型“请必须返回符合某种 JSON 格式数据”的底层提示词。
# =====================================================================
prompt = PromptTemplate(
    template="分析一下当前热门的技术栈。\n{format_instructions}\n目标技术: {topic}",
    input_variables=["topic"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)
print(parser.get_format_instructions())
# 4.初始化模型
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.2)
# =====================================================================
# 5. 组装 LCEL 链
# 此时的流水线终点变成了 parser，它会自动捕获模型的文本输出并转换为 Pydantic 对象
# =====================================================================
chain = prompt | llm | parser

# 6.运行链
output = chain.invoke({"topic": "Langchain"})

# =====================================================================
# 7. 验证输出结果
# =====================================================================
print(f"返回的数据类型: {type(output)}")
print(f"技术名称: {output.language}")
print(f"核心优势: {output.advantages}")
print(f"学习难度: {output.difficulty_level}")
