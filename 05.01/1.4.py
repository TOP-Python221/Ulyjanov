s = ord(input())
n = int(input())
s2 = ord(input())
n2 = int(input())
if s == s2 and n == n2 - 1 or n == n2 + 1:
    print("Да")
elif s == s2 - 1 and n == n2 - 1 or n == n2 + 1 or n == n2:
    print("Да")
elif s == s2 + 1 and n == n2 - 1 or n == n2 + 1:
    print("Да")
else:
    print("Нет")


# вывод 1

# g
# 3
# f
# 2
# Да

# вывод 2

# с
# 6
# в
# 4
# Нет