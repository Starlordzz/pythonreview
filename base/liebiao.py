shopping_list = ["apple", "banana", "orange", "grape", "watermelon"]
shopping_list.append(input("Please enter your name: "))
print(shopping_list)
shopping_list.sort()
#打乱shopping_list的顺序
import random
random.shuffle(shopping_list)
print(shopping_list)
print(shopping_list[1])
