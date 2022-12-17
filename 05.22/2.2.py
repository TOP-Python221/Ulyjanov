from random import choice

l = []
all_trying = 0
trying = 0
p = 0
o = 0

for i in range(10):
    while True:
        trying += 1
        all_trying += 1
        f = choice(('O', 'P'))
        l.append(f)
        if f == 'P':
            p = p + 1
            o = 0
        else:
            o += 1
            p = 0
        if o == 3 or p == 3:
            print(f'{l} (число попыток: {trying})')
            l = []
            trying = 0
            break
print(f'Среднее число попыток: {all_trying / 10}')
