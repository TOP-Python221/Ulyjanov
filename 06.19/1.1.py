
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
11111111
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
GCD = gcd(a, b)
print(GCD)

# вывод
#
# Введите первое число: 5
# Введите второе число: 15
# 5