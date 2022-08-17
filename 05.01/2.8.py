num1 = 1
num2 = 1
num3 = 0
i = int(input())
if i == 1:
    print(i)
else:
    print(num1, num2, end=" ")
    for j in range(2, i):
        num3 = num1 + num2
        print(num3, end=" ")
        num2 = num1
        num1 = num3
    
#  вывод 1:
# 1
# 1
#  вывод 2:
# 17
# 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597