sum = 0
i = 1
d = 0
num = int(input("Введите число "))
while i <= num:
    d = num % i
    if d == 0:
        sum += i
    i += 1
print(sum)