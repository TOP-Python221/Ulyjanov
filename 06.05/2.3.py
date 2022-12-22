s = input('Введите строку: ')
s1 = input('Введите вторую строку: ')
l = [' ', ',', '.']
d = {}
d2 = {}
for ch in s.lower():
    if ch not in l:
        if ch in d:
            d[ch] = d[ch] + 1
        else:
            d[ch] = 1

for ch in s1.lower():
    if ch not in l:
        if ch in d2:
            d2[ch] = d2[ch] + 1
        else:
            d2[ch] = 1

if d == d2:
    print('Введеные слова являются анаграммами.')
else:
    print('Введенные слова не являются аннаграммами.')