from random import choice

l=[]
all_trying = 0
trying = 0
p = 0
o = 0

for i in range(10):
    while True:
        f = choice(('O', 'P'))
        trying += 1
        all_trying += 1
        if f == 'P':
            p += 1
            l.append(f)
            o = 0
        else:
            o += 1
            l.append(f)
            p = 0
        if p == 3 or o == 3:
            print(f'{l} (число попыток: {trying})')
            l = []
            trying = 0
            break
print(f'Среднее число попыток: {all_trying / 10}')