numb1_str = input("Введите первое число ")
numb2_str = input("Введите второе число ")
numb1 = int(numb1_str)
numb2 = int(numb2_str)
fl = numb1 / numb2
k = int(float(fl))
i = k % 2
if i == 0:
    print(f"{numb1} делится на {numb2} нацело")
    print(f"частное: {k}")
else:
    print(f"{numb1} не делится на {numb2} нацело")
    print(f"частное: {k}")
    print(f"Остаток: {i}")