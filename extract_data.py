import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

user_input = "我是大师傅，服了，电话号码是123-456-7890，地址在北京市朝阳区幸福大街88号，谁把我电脑屏幕弄花了你们我真的服了不想聊了都！"


system_prompt = """"你是一个数据提取助手，专门从杂乱无章的文本中提取有用的信息。包含 1 name 2 phone 3 issue 4 sentiment"
⚠️ 重要要求：
- 必须直接返回 JSON 格式数据。
- 不要包含 markdown 标记（如 ```json ... ```）。
- 不要说“好的”、“如下所示”等废话。"""
print("reading...")

completion = client.chat.completions.create(
    model="qwen-plus",
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_input}
    ]
)
ai_text = completion.choices[0].message.content

try:
    data_dict = json.loads(ai_text)
    print("=" * 20)
    print(f"客户姓名：{data_dict['name']}")
    print(f"客户电话：{data_dict['phone']}")
    print(f"客户需求：{data_dict['issue']}")
    print(f"客户情绪：{data_dict['sentiment']}")
    print("=" * 20)
except json.JSONDecodeError:
    print("❌ 出错了：AI 返回的不是合法的 JSON，没法解析。")