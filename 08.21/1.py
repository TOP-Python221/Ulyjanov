import math


# ДОБАВИТЬ: документацию класса
class Tetrahedron:
    def __init__(self, side: int):
        self.side = side
        # нахождение площади правильного тетраэдра
        self.area = self.side**2 * math.sqrt(3)
        # нахождение объема тетраэдра
        self.volume = math.sqrt(2)/12 * self.side ** 3

    def __str__(self):
        return f'площадь правильного тетраэдра = {self.area:.2f}\n' \
               f'объём правильного тетраэдра = {self.volume:.2f}'


tr1 = Tetrahedron(5)
print(tr1)

# stdout:
# площадь правильного тетраэдра = 43.30
# объем правильного тетраэдра = 14.73

# ИТОГ: всё верно — 5/5
