#写一段代码让我彻底了解python测试
# Python测试通常使用unittest或pytest框架。下面是一个使用unittest框架的简单示例，帮助你了解Python测试的基本概念。
import unittest

# 被测试的函数
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
# 测试类
class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(multiply(4, 5), 20)
        self.assertEqual(multiply(-1, 1), -1)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertRaises(ValueError, divide, 10, 0)
# 运行测试
if __name__ == '__main__':
    unittest.main()
# 运行上述代码时，unittest框架会自动发现并运行TestMathOperations类中的所有测试方法（以test_开头的方法）。每个测试方法使用断言（如self.assertEqual）来验证函数的输出是否符合预期。如果所有断言都通过，测试将成功；如果有任何断言失败，测试将报告失败。