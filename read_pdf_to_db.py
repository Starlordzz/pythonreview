import pdfplumber
import chromadb
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client_openai = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)


# === 1. 定义读取 PDF 的函数 (眼睛) ===
def extract_text_from_pdf(pdf_path):
    print(f"📖 正在读取 {pdf_path} ...")
    full_text = ""
    # 打开 PDF 文件
    with pdfplumber.open(pdf_path) as pdf:
        # 遍历每一页
        for page in pdf.pages:
            # 提取这一页的文字
            text = page.extract_text()
            if text:
                full_text += text + "\n"
    return full_text


# === 2. 定义切片函数 (切香肠) ===
# 这是一个简单的切法：每 300 个字切一刀
# 以后用了 LangChain，它有更高级的切法（比如按句号切）
def split_text(text, chunk_size=300):
    chunks = []
    # range(开始, 结束, 步长)
    for i in range(0, len(text), chunk_size):
        # 截取从 i 到 i+300 的文字
        chunk = text[i: i + chunk_size]
        chunks.append(chunk)
    return chunks


# === 3. 嵌入函数 (还是那个配方) ===
def get_embedding(text):
    return client_openai.embeddings.create(
        model="text-embedding-v1",
        input=text
    ).data[0].embedding


# === 主程序 ===
if __name__ == "__main__":
    # A. 准备工作
    pdf_filename = "data.pdf"  # ⚠️ 确保你放了这个文件！

    # 检查文件是否存在，防止报错
    if not os.path.exists(pdf_filename):
        print(f"❌ 错误：找不到 {pdf_filename}，请把文件放进项目文件夹！")
        exit()

    # B. 读取与切片
    raw_text = extract_text_from_pdf(pdf_filename)
    print(f"✅ 读取成功！共 {len(raw_text)} 个字。")

    chunks = split_text(raw_text, chunk_size=300)
    print(f"🔪 切片完成！共切成了 {len(chunks)} 段。")

    # C. 存入数据库
    print("🚀 正在存入 ChromaDB...")

    chroma_client = chromadb.PersistentClient(path="./my_knowledge_db")

    # 为了避免 ID 冲突，我们这次新建一个 collection 叫 'pdf_data'
    # 如果已存在先删除（方便你反复测试）
    try:
        chroma_client.delete_collection("pdf_data")
    except:
        pass

    collection = chroma_client.create_collection(name="pdf_data")

    # 批量计算向量并存储
    # 注意：如果 PDF 很大，这里可能要跑一会儿
    ids = [f"chunk_{i}" for i in range(len(chunks))]
    embeddings = [get_embedding(chunk) for chunk in chunks]

    collection.add(
        documents=chunks,
        embeddings=embeddings,
        ids=ids
    )

    print("🎉 全部完成！你的 PDF 已经被 AI 记住了。")