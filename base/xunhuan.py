ex = 0
while ex != 1:
    i=0
    input_num = []
    input_num.append(float(input("Please enter a number: ")))
#写一个平均值 输入到列表中 列表的和/长度 用while循环和列表实现，接着上边的代码
    while i != -1:
        next_num = input("Please enter another number (or type 'done' to finish): ")
        if next_num.lower() == 'done':
            i = -1
        else:
            input_num.append(float(next_num))
    average = sum(input_num) / len(input_num)
    print("The average of the entered numbers is: " + str(average))
    ex = int(input("Type 1 to exit or 0 to continue: "))



