import math


class Tetraider:
    def __init__(self, side: int):
        self.side = side
        # нахождение площади правильного тетраэдера
        self.area = (self.side ** 2) * math.sqrt(3)
        # нахождение объема тетраэдера
        self.volume = math.sqrt(2)/12 * self.side ** 3

    def __str__(self):
        return (f'площадь правильного тетраэдра = {self.area:.2f}\nобъем правильного тетраэдера = {self.volume:.2f}')


tr1 = Tetraider(5)
print(tr1)

# вывод функции print
# площадь правильного тетраэдра = 43.30
# объем правильного тетраэдера = 14.73