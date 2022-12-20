d = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 5}
keys = []
values = int(input('Введите цифру занчение которой нужно найти:'))
for key in d:
    if d[key] == values:
        keys.append(key)
print(keys)