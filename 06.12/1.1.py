day = int(input('Введите номер дня: '))
monts = int(input('Введите номер месяца: '))
year = int(input('Введите год: '))

def ordinalDate(day,monts,year):
    summ_day = 0
    flag = True
    l = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if monts <=0:
        return 'Номер месяца не может быть меньше 0 '
    elif monts > 12:
        return 'Номер месяца не может быть больше 12 '
    elif day <=0:
        return 'Номер для не может быть отрецательным'
    elif day > 31:
        return 'число для не может превышать 31го'
    # определение високосного года
    if (year % 4 == 0 or year % 400 == 0) and year % 100 != 0:
        flag = True
        l[1] = 29
    else:
        flag = False
    if monts == 2 and day > 28 and flag == False:
        return 'В этом году в феврале 28 дней'
    for i in range(monts - 1):
        summ_day = summ_day + l[i]
    summ_day += day
    return f'порядковый номер дня {summ_day}'

print(ordinalDate(day, monts, year))


# вывод

#порядковый номер дня 316

