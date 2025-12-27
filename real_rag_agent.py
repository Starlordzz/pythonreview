import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

# === 1. 模拟企业海量知识库 ===
# 想象这里有 1000 条数据
knowledge_base = [
    "公司的WIFI密码是: 12345678。",
    "行政部在3楼，技术部在4楼，财务部在5楼。",
    "报销流程：先填单子，找主管签字，最后去财务部。",
    "老板最讨厌别人迟到，迟到一次扣500块。",
    "公司的午休时间是 12:00 到 13:30。"
]

# 缓存所有知识库的向量 (真实项目中，这一步会存到数据库里，不需要每次都算)
print("📚 正在构建向量索引 (初始化)...")
kb_vectors = [client.embeddings.create(model="text-embedding-v3", input=doc).data[0].embedding for doc in
              knowledge_base]
print("✅ 索引构建完成！")


def search_relevant_doc(query):
    """ 去知识库里捞最相关的一条 """
    # 1. 把问题变向量
    query_vec = client.embeddings.create(model="text-embedding-v3", input=query).data[0].embedding
    print(query_vec)
    # 2. 算分
    scores = cosine_similarity([query_vec], kb_vectors)[0]
    print(scores)
    # 3. 找到最高分的索引
    best_idx = np.argmax(scores)

    # 4. 只有当分数够高（比如大于 0.4）才算找到，否则算没找到
    if scores[best_idx] < 0.4:
        return None

    return knowledge_base[best_idx]


# === 主程序 ===
while True:
    user_query = input("\n请提问 (输入 q 退出): ")
    if user_query == 'q': break

    # Step 1: 检索 (Retrieve)
    print(f"🔍 正在知识库中搜索答案...")
    found_doc = search_relevant_doc(user_query)

    if found_doc:
        print(f"📖 检索到的参考资料: {found_doc}")
        # Step 2: 增强 (Augment) & 生成 (Generate)
        prompt = f"""
        你是一个企业助手。请根据下面的【内部资料】回答员工问题。

        【内部资料】：
        {found_doc}

        【员工问题】：
        {user_query}
        """
    else:
        print("⚠️ 知识库里没找到相关内容，依靠 AI 自身知识回答。")
        prompt = user_query

    # Step 3: 调用大模型
    completion = client.chat.completions.create(
        model="qwen-plus",
        messages=[{"role": "user", "content": prompt}]
    )

    print(f"🤖 AI 回答: {completion.choices[0].message.content}")