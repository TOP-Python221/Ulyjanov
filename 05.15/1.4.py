a = input()
sum = 0
sum2 = 0
g = a[:3]
b = a[3:]
for i in g:
    sum += int(i)
for j in b:
    sum2 += int(j)
if sum == sum2:
    print("Да")
else:
    print("Нет")

# 183534
# Да

# 455555
# Нет