from random import randrange

l1 = []
l2 = []
set1 = set()
summ = 0
for _ in range(20):
    l1.append(randrange(0, 20))
    l2.append(randrange(0, 20))

set1 = set(l1)
set1 = set(l2)
print(set1)

# вывод
#{0, 1, 2, 3, 4, 5, 6, 8, 9, 11, 12, 13, 14, 15, 17, 18, 19}