m = ''
p= " "
x = True
while x:
    r =int(input())
    if r % 7 == 0:
        m += str(r) + p
    else:
        x = False
print(m)

# Вывод

# 7
# 7
# 14
# 21
# 5
# 7 7 14 21