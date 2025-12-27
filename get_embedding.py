import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

def get_embedding(text):
    # 调用专门的 embedding 模型
    # 阿里通常使用 text-embedding-v1 或 v2
    response = client.embeddings.create(
        model="text-embedding-v3",
        input=text
    )
    # 返回那串长长的数字
    return response.data[0].embedding

# 测试一下
text = "苹果"
vector = get_embedding(text)

print(f"文字：{text}")
print(f"向量维度(数字的个数)：{len(vector)}")
print(f"前 5 个数字长这样：{vector[:5]}")