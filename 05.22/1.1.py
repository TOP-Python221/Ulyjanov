l = []
nums = input('Введите число:')
while nums !='':
    num = int(nums)
    l.append(num)
    nums = input('Введите число (Для завершения нажмите Enter: ')

if len(l) < 4:
    print('Вы ввели меньше четырех чисел')
else:

    sort_list = sorted(l)
    print(f'исходный список{sort_list}')
    sort_list.pop()
    sort_list.pop(0)
    print(f'Список с удаленными наибольшим и наименьшим значением {sort_list}')