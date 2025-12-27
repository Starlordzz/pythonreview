import json
import os
from openai import OpenAI
from dotenv import load_dotenv



# 1. 配置环境
load_dotenv()
client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

def get_weather(city):
    # 这里是一个模拟的天气数据查询函数
    # 在真实应用中，你可能会调用一个天气 API
    weather_data = {
        "北京": "晴，25°C",
        "上海": "多云，28°C",
        "广州": "雷阵雨，30°C"
    }
    return weather_data.get(city, "抱歉，我没有该城市的天气信息。")

system_prompt = """
你是一个全能助手。
如果用户问天气，请务必只输出 JSON：{"action": "get_weather", "city": "城市名"}
如果用户只是闲聊，请直接回答。
"""

messages = [
    {"role": "system", "content": system_prompt}
]

user_query = input()

messages.append({"role": "user", "content": user_query})

completion = client.chat.completions.create(
    model="qwen-plus",
    messages=messages
)
ai_response = completion.choices[0].message.content
print(f"AI 原始回复: {ai_response}")

try:
    action_data = json.loads(ai_response)
    if action_data["action"] == "get_weather":
        city = action_data["city"]
        weather_info = get_weather(city)

        messages.append({"role": "assistant", "content": ai_response})
        messages.append({"role": "system", "content": f"工具运行结果{weather_info}"})

        final_completion = client.chat.completions.create(
            model="qwen-plus",
            messages=messages
        )
        finanl_answer = final_completion.choices[0].message.content
        print(f"🤖 AI 最终回复:\n{finanl_answer}")
    else:
        # 如果是 JSON 但不是天气请求，或者格式不对，直接打印
        print(f"AI 回复: {ai_response}")
except json.JSONDecodeError:
    print("AI 回复不是合法的 JSON，直接输出回复内容：")
    print(ai_response)