day = int(input('Введите номер дня: '))
month = int(input('Введите номер месяца: '))
year = int(input('Введите год: '))

def ordinalDate(day,month,year):
    summ_day = 0
    flag = True
    l = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if month <=0:
        return 'Номер месяца не может быть меньше 0 '
    elif month > 12:
        return 'Номер месяца не может быть больше 12 '
    elif day <=0:
        return 'Номер для не может быть отрицательным'
    elif day > 31:
        return 'число для не может быть больше 31'
    # определение високосного года
    if (year % 4 == 0 or year % 400 == 0) and year % 100 != 0:
        flag = True
        l[1] = 29
    else:
        flag = False
    if month == 2 and day > 28 and flag == False:
        return 'В этом году в феврале 28 дней'
    for i in range(month - 1):
        summ_day = summ_day + l[i]
    summ_day += day
    return f'порядковый номер дня {summ_day}'

print(ordinalDate(day, month, year))


# вывод

#порядковый номер дня 316

