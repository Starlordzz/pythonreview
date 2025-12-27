import os
from openai import OpenAI
from dotenv import load_dotenv

# 1. 配置环境
load_dotenv()
client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

# 2. 初始化记忆列表 (这是关键！一开始只有人设)
# 你可以改改 content，让它扮演不同的角色
messages = [
    {"role": "system", "content": "你是一个热情且有点话唠的 AI 助手，喜欢在每句话结尾加 emoji。"}
]

print("=== AI 聊天机器人已启动 (输入 'quit' 退出) ===")

# 3. 开启无限循环
while True:
    # --- A. 获取用户输入 ---
    user_text = input("\n你: ")  # 程序会在这里暂停，等你打字按回车

    # 如果用户输入 quit，就打破循环，结束程序
    if user_text == "quit":
        print("AI: 拜拜！下次再聊！👋")
        break

        # --- B. 把你的话加入记忆列表 ---
    # 这一步如果不做，AI 就不知道你刚才说了什么
    messages.append({"role": "user", "content": user_text})

    # --- C. 发送整个列表给 AI ---
    # 注意：这里传进去的是整个 messages 列表，包含了之前的历史
    completion = client.chat.completions.create(
        model="qwen-plus",
        messages=messages
    )


    # --- D. 获取 AI 的回答 ---
    ai_text = completion.choices[0].message.content
    print(f"AI: {ai_text}")

    # --- E. 把 AI 的回答也加入记忆列表 (至关重要！) ---
    # 如果不把 AI 说的话存进去，它下次就会忘了自己说过什么
    messages.append({"role": "assistant", "content": ai_text})