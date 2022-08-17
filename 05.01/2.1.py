
k = "КУЗЬМА"
for i in k:
    if i == "К":
        j = 6
        a = 2
    elif i == "У":
        j = 1
        a = 5
    elif i == "З":
        j = 3
        a = 3
    elif i == "Ь":
        j = 1
        a = 1
    elif i == "М":
        j = 7
        a = 4
    elif i == "А":
        j = 1
        a = 7
    for j2 in range(j):
        for a2 in range(a):
            print(i, end="")
        print()

# вывод

# КК
# КК
# КК
# КК
# КК
# КК
# УУУУУ
# ЗЗЗ
# ЗЗЗ
# ЗЗЗ
# Ь
# ММММ
# ММММ
# ММММ
# ММММ
# ММММ
# ММММ
# ММММ
# ААААААА