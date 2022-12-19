l = []
less = []
equal = []
more = []
amount_num = 0
summ = 0
nums = input('Введите число: ')
while nums != '':
    nums = float(nums)
    l.append(nums)
    nums = input('Введите число (Для завершения нажмите Enter: ')

for i in l:
    amount_num += 1
    summ = summ + i

summ = summ / amount_num

for i in l:
    if i < summ:
        less.append(i)
    elif i > summ:
        more.append(i)
    else:
        equal.append(i)

print(f'Числа ниже среднего: {less}')

if equal == []:
    print('Равных чисел нет')
else:
    print(f'Числа раные среднему: {equal}')

print(f'Числа больше среднего: {more}')