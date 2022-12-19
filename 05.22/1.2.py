negative = []
zero = []
positive = []

nums = input('Введите целое число (Нажмите Enter для окончания ввода: ')
while nums != '':
    nums = int(nums)
    if nums < 0:
        negative.append(nums)
    elif nums > 0:
        positive.append(nums)
    else:
        zero.append(nums)
    nums = input('Введите целое число (Нажмите Enter для окончания ввода: ')
print(f'Отрицательные заняения {negative}')
print(f'Нули {zero}')
print(f'Положительные заначения {positive}')