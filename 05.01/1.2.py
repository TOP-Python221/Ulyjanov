ear = int(input("Введите год "))
if ear % 4 == 0 or ear % 400 == 0:
    print("Да")
elif ear % 100 !=0:
    print("Нет")