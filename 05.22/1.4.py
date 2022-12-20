summ = 0
words = input('Введите числа в строку через пробел: ')
words = words.split()
for i in range(0, len(words) - 1):
    if int(words[i]) < int(words[i+1]):
        summ += 1

print(f'Количество элементов списка больших предидущего: {summ}')