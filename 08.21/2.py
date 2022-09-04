import datetime

class TimeZone:
    def time(self):
        """ метод для вычисления времени в заданном часовом поясе """
        offset = datetime.timedelta(hours=self.offset)
        tz = datetime.timezone(offset, name=self.nemetimezone)
        dt = datetime.datetime.now(tz=tz)
        tz.utcoffset(dt)
        return dt

    def daytime(self):
        """ метод для определения времени суток """
        timenow = str(self.time()).split()
        timenow = timenow[1].split(':')
        hours = int(timenow[0])
        if hours >= 5 and hours < 12:
            return 'Сейчас утро'
        elif hours >= 12 and hours < 16:
            return 'Сейчас день'
        elif hours >= 16 and hours <24:
            return 'Сейчас вечер'
        else: return 'Сейчас ночь'

    def __init__(self, offset: int, nemetimezone: str):
        # свойство экземпляра для задания названия часового пояса
        self.nemetimezone = nemetimezone
        self.offset = offset
        self.timenow = self.daytime()

    def __str__(self):
        return f'{self.timenow}\n{self.time()} {self.nemetimezone}'
tz = TimeZone(4, 'utc')
print(tz)

# Сейчас утро
# 2022-08-25 09:13:55.921148+04:00