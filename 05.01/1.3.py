a = ''
while a !="n":
    g = input("Введите координату по горизонтали ")
    v = input("Введите координату по вертикали ")
    g2 = input("Введите координату 2 по горизонтали ")
    v2 = input("Введите координату 2 по вертикали ")
    if v == v2 or g == g2:
        print("Да")
    else:
        print("Нет")
    a = input("Для завершения введте n ")