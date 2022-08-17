
exit = ""
sum = 0
while exit != "n":
    num = int(input("Введите число "))
    if num > 0:
        sum += num
    exit = input("Для окончания ввода нажмите 'n '")
print(sum)