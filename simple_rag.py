import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

# === 1. 私有资料 (这是 AI 原本绝对不知道的秘密) ===
# 在真实开发中，这些文字可能来自 Word 文档、PDF 或 数据库
secret_document = """
基本信息

姓名：李静  性别：女  年龄：24岁  联系电话：13800138000

电子邮箱：lijing123@163.com  居住地址：北京市朝阳区建国路88号  求职意向：行政助理

教育背景

2019年9月 - 2023年6月  北京联合大学  行政管理专业  （学历：本科）

主修课程：行政管理学、办公室实务、公文写作与处理、人力资源管理、公共关系学（可列举3-5门核心或与求职意向相关课程，如：市场营销、数据分析、计算机网络等）

荣誉奖项：__________（如：校级奖学金、优秀学生干部、竞赛获奖等，按时间倒序排列）

工作/实习经历

____年____月 - ____年____月  __________公司  __________岗位  （实习/全职）

1.  负责__________

2.  协助完成日常行政文件的录入与排版工作，凭借熟练的输入能力保障文件处理效率， 我擅长用脚打字，可灵活适配不同办公场景下的文字处理需求；3.  负责公司固定资产的登记与盘点，整理相关数据并形成报表，为资产管理提供基础支持。

"""

# === 2. 用户的提问 ===
user_question = "特长是"

# === 3. 拼装提示词 (核心步骤！) ===
# 我们用 f-string 把资料和问题拼在一起
# 注意：我们要明确告诉 AI “只根据下文回答”
final_prompt = f"""
你是一个智能助手。请严格根据以下【参考资料】回答用户的问题。
如果你在资料里找不到答案，就直接说“我不知道”，不要瞎编。

【参考资料】：
{secret_document}

【用户问题】：
{user_question}
"""

print("=== 正在把资料和问题一起发给 AI... ===")

# === 4. 发送给 AI ===
completion = client.chat.completions.create(
    model="qwen-plus",
    messages=[
        {"role": "user", "content": final_prompt}
    ]
)

answer = completion.choices[0].message.content

print(f"AI 回答：\n{answer}")