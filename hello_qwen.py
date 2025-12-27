import os
from openai import OpenAI
from dotenv import load_dotenv

# 1. 打开保险箱，读取密码
# 这行代码会自动去 .env 文件里找配置
load_dotenv()

# 2. 创建一个“电话机” (Client)
# 这一步是最关键的！
client = OpenAI(
    # 从保险箱里取出阿里的 Key
    api_key=os.getenv("DASHSCOPE_API_KEY"),

    # 🚨 重点：把电话线插到阿里的服务器上 (这叫 Base URL)
    # 如果不写这行，它就会默认去连美国的 OpenAI，那就报错了
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

# 3. 准备你要说的话
print("正在呼叫 Qwen 通义千问...")

# 4. 拨通电话，开始对话
completion = client.chat.completions.create(
    # 这里的 model 必须写阿里支持的名字，比如 "qwen-plus" 或 "qwen-max"
    model="qwen-plus",

    messages=[
        # system: 给 AI 的人设（你是谁）
        {'role': 'system', 'content': '你是一个非常友好的编程助教，说话要风趣幽默。'},
        # user: 你说的话
        {'role': 'user', 'content': '你好！请用一句话通过比喻解释什么是 Python？'}
    ]
)

# 5. 获取并打印回答
# 这是一个像洋葱一样的结构，我们要一层层剥开拿到内容
ai_reply = completion.choices[0].message.content

print("=" * 20)
print(f"Qwen 回答：\n{ai_reply}")
print("=" * 20)