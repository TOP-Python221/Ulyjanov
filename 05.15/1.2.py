price = 0
s = input()
p = s.split()
for i in p:
    for j in i:
        price += 1
print(f'{(price * 80)//100} руб. {(price * 80) % 100} коп.')

# грузите апельсины бочках братья карамазовы
# 30 руб 40 коп.