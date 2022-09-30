import datetime


class TimeZone:
    # КОММЕНТАРИЙ: специальные методы мы размещаем наверху, пока нет весомых причин сделать иначе
    def __init__(self, offset: int, tz_name: str):
        # атрибут экземпляра для задания названия часового пояса
        self.tz_name = tz_name
        self.offset = offset
        self.daypart = self.daytime()

    def __str__(self):
        return f'{self.daypart}\n{self.time()} {self.tz_name}'

    def daytime(self):
        """ метод для определения периода суток """
        now = str(self.time()).split()
        now = now[1].split(':')
        hours = int(now[0])
        # ИСПОЛЬЗОВАТЬ: как это вы пропустили, что Python позволяет записывать неравенства математически?
        if 5 <= hours < 12:
            return 'Сейчас утро'
        elif 12 <= hours < 16:
            return 'Сейчас день'
        elif 16 <= hours < 24:
            return 'Сейчас вечер'
        else:
            return 'Сейчас ночь'

    def time(self):
        """ метод для вычисления времени в заданном часовом поясе """
        offset = datetime.timedelta(hours=self.offset)
        tz = datetime.timezone(offset, name=self.tz_name)
        dt = datetime.datetime.now(tz=tz)
        tz.utcoffset(dt)
        return dt


tz1 = TimeZone(5, 'utc')
print(tz1)


# tests:
# Сейчас утро
# 2022-08-25 09:13:55.921148+04:00
