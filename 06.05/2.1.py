s = input('Введите строку: ')
d =  {}
for ch in s:
    d[ch] = 'unique'

print(f'В сроке {s}, {len(d)} уникальных символов')