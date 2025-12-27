import os
import json
from openai import OpenAI
from dotenv import load_dotenv


# 1. 配置环境
load_dotenv()
client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

def weather(city):
    print(f"Fetching weather for {city}...")
    # Simulated weather data
    if "Beijing" in city:
        return f"The current weather in Beijing is sunny with a temperature of 25°C."
    else:
        return f"Sorry, I don't have weather data for {city}."

def calculater(expression):
    try:
        result = eval(expression)
        return f"The result of {expression} is {result}."
    except Exception as e:
        return f"Error calculating expression: {str(e)}"
# 2. 准备对话内容
system_prompt = """你是一个智能助手，可以调用工具来帮助用户完成任务。
当用户询问天气时，给出一下json格式 不要说其他的东西{"action":"get_weather","city":"城市名"}
如果用户询问计算结果 给出一下json格式不要说其他东西 {"action":"calc","expression":"计算表达式"}
如果用户只是闲聊，请直接回答。"""

user_query = input()

completion = client.chat.completions.create(
    model="qwen-plus",
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_query}
    ]
)

ai_response = completion.choices[0].message.content

print(f"original_ai_response{ai_response}")

try:
    action = json.loads(ai_response)
    if action["action"] == "get_weather":
        city = action["city"]
        weather_info = weather(city)
        print(weather_info)
    elif action["action"] == "calc":
        expression = action["expression"]
        calc_result = calculater(expression)
        print(calc_result)
    else:
        print("Unknown action.")
except json.JSONDecodeError:
    print("=" * 20)
    print(f"{ai_response}")
    print("=" * 20)



