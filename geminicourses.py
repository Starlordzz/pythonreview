# ==============================================================================
# AI 学习代码示例集合
# ==============================================================================

# ------------------------------------------------------------------------------
# 示例 1: Token 计算
# ------------------------------------------------------------------------------
"""
input_tokens = 50
output_tokens = 100
total = input_tokens + output_tokens
print(total)
"""

# ------------------------------------------------------------------------------
# 示例 2: 翻译提示词生成
# ------------------------------------------------------------------------------
"""language = "english"
text = "i love learning ai"
final_prompt = f"请作为专业翻译，将以下内容翻译为{language}：{text}"
print(final_prompt)
"""

# ------------------------------------------------------------------------------
# 示例 3: 工具列表操作
# ------------------------------------------------------------------------------
"""
tools = ["google search" , "计算器" , "翻译"]
print(f"the first tool i use is {tools[0]}")
"""

# ------------------------------------------------------------------------------
# 示例 4: 对话历史记录
# ------------------------------------------------------------------------------
"""
history = []
history.append("how about the 股票 today")
history.append("大盘正在上涨")
print(history[1])
"""

# ------------------------------------------------------------------------------
# 示例 5: AI 配置字典
# ------------------------------------------------------------------------------
"""ai_config = {
    "model": "gpt-4",
    "temperature": 0.7,}
print(f"currently using model:{ai_config['model']}, temperature:{ai_config['temperature']}")
"""

# ------------------------------------------------------------------------------
# 示例 6: Token 统计分析
# ------------------------------------------------------------------------------
"""token_list = [200,500,400]
total_tokens = 0
for token in token_list:
    total_tokens += token
print(f"total tokens used: {total_tokens}")
print(f"average tokens per request: {total_tokens / len(token_list)}")"""

# ------------------------------------------------------------------------------
# 示例 7: 提示词生成函数
# ------------------------------------------------------------------------------
"""def make_prompt(user_question):
    context = f"you are a helpful ai assistant. answer the question based on the following context: {user_question}"
    return context
final_prompt = make_prompt("why is the sky blue?")
print(final_prompt)"""

# ==============================================================================
# 当前激活的代码: AI 响应模拟器
# ==============================================================================

import time
import random

# 定义 AI 思考状态的响应列表
response = ["thinking...", "let me see...", "analyzing data..."]

# 模拟 AI 思考过程
"""for i in range(len(response)):
    # 随机选择一个响应并显示
    print(random.choice(response))

    # 生成 1-3 秒的随机等待时间
    int1 = random.randint(1, 3)

    # 暂停执行
    time.sleep(int1)

    # 显示等待时长
    print(f"waited for {int1} seconds")"""

# ==============================================================================


class Role:
    def __init__(self,name,hp):
        self.name = name
        self.hp = hp
    def attack(self,damage):
        self.hp = self.hp - damage
        print(f"{self.name} was attacked and lost {damage} hp. Remaining hp: {self.hp}")

# 创建角色实例
boss = Role("boss" ,100)
boss.attack(30)
boss.attack(40)
