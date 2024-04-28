class Time:
    __time = 86400

    def __init__(self, sec):
        if type(sec) != int:
            raise TypeError('Секунды - целое число')
        self.sec = sec % self.__time

    @classmethod
    def __get_form(cls, x):
        return str(x).rjust(2, '0')

    def  __add__(self, other):
        if type(other) != int:
            raise TypeError('Секунды - целое число')
        return Time(self.sec + other)

    def get_time(self):
        s = self.sec % 60
        n = (self.sec // 60) % 60
        h = (self.sec // 3600) % 24
        return f'{self.__get_form(h)}:{self.__get_form(n)}:{self.__get_form(s)}'

t1 = Time(1000)
t1 += 100
print(t1.get_time())