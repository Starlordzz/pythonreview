import chromadb
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client_openai = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

# === 1. 定义嵌入函数 (还是用阿里的) ===
def get_embedding(text):
    return client_openai.embeddings.create(
        model="text-embedding-v3",
        input=text
    ).data[0].embedding

# === 2. 初始化 ChromaDB (持久化模式) ===
# path="my_knowledge_db" 意思是：在当前目录下生成一个文件夹存数据
chroma_client = chromadb.PersistentClient(path="./my_knowledge_db")

# === 3. 创建/获取一个集合 (Collection) ===
# 名字随便起，比如 "company_rules"
collection = chroma_client.get_or_create_collection(name="company_rules")

# === 4. 准备要存的数据 ===
documents = [
    "公司的WIFI密码是: 12345678。",
    "行政部在3楼，技术部在4楼。",
    "老板最讨厌迟到，迟到扣500。",
    "LangChain 是一个开发 LLM 应用的框架。",
    "ChromaDB 是一个轻量级向量数据库。"
]

# === 5. 开始存入 (Add) ===
print("🚀 开始将数据写入硬盘...")

# 我们需要给每一条数据一个唯一的 ID，这里简单用 "id1", "id2"...
ids = [f"id{i}" for i in range(len(documents))]

# 计算向量
embeddings = [get_embedding(doc) for doc in documents]

# 存入数据库
collection.add(
    documents=documents,   # 原文 (方便以后查看)
    embeddings=embeddings, # 向量 (用于搜索)
    ids=ids                # 身份证号
)

print(f"✅ 成功存入 {len(documents)} 条数据！")
print("📁 数据已保存在 ./my_knowledge_db 文件夹中。")