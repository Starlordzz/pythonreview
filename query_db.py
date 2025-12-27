import chromadb
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client_openai = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

def get_embedding(text):
    return client_openai.embeddings.create(
        model="text-embedding-v3",
        input=text
    ).data[0].embedding

# === 1. 重新连接数据库 ===
# 指向同一个文件夹，它会自动读取里面的数据
chroma_client = chromadb.PersistentClient(path="./my_knowledge_db")

# === 2. 获取之前的集合 ===
collection = chroma_client.get_collection(name="company_rules")

# === 3. 用户提问 ===
user_query = "老板讨厌什么？"
print(f"🔍 问题: {user_query}")

# === 4. 在数据库中搜索 (Query) ===
# ChromaDB 帮我们做好了余弦相似度计算，不需要 numpy 了
results = collection.query(
    query_embeddings=[get_embedding(user_query)], # 把问题变成向量传进去
    n_results=1 # 只找最相似的 1 条
)

# === 5. 解析结果 ===
# results 是一个字典，包含 ids, documents, distances 等
best_doc = results['documents'][0][0] # 结构有点深，这是两层列表

print(f"📖 检索到的答案: {best_doc}")