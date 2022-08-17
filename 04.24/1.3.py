import sys
time = input("Введите количество минут: ")
hours = int(int(time) / 60)
minut = int(int(time) % 60)
print(hours,minut)
if int(hours) >= 11 and int(hours)<= 20:
    print(hours, "часов", minut, "мин")
    sys.exit()
m = int(minut) % 10
if m == 0 or m >4:
    mm = "минут"
else:
    mm = "минуты"
b = int(hours) % 10
if b == 0 or b >=5 and b <=9:
    print(hours, "часов", minut, mm)
elif b > 1 and b < 5:
    print(hours, "часа", minut, mm)
elif b == 1:
    print(hours, "час", minut, mm)

