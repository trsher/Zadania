import math

tf = True       #Переменная для проверки точки
class Otrezok:      #Объявление класса


    def __init__(self, point1, point2):     #При создании объекта
        if isinstance(point1, list) and isinstance(point2, list) and len(point1) == 2 and len(point2) == 2:
            self.__point1 = point1
            self.__point2 = point2
        else:
            print("Введите данные заного")
            tf = False


    def get_point1(self):           #Вывод 1 точки
        if tf:
            return self.__point1

    def set_point1(self):       #Ввод 1 точки
        if tf:
            x1 = int(input("Введите х: "))      #Ввод первой координаты точки
            y1 = int(input("Введите у: "))      #Ввод второй координаты точки
            L = math.sqrt((self.__point1[0] - self.__point2[0])**2 + (self.__point1[0] - self.__point2[0])**2)
            print(f"Длина равна: {round(L,3)}")     #Вывод длины отрезка
            self.__point1[0] = x1
            self.__point1[1] = y1
            f = math.atan((y1-self.__point2[1])/(x1-self.__point2[0]))      #Формула расчета изменения координаты
            self.__point2[0] = L*math.cos(f)+ x1
            self.__point2[1] = L*math.sin(f)+ y1

    def get_point2(self):           #Вывод 2 точки
        if tf:
            return self.__point2

    def set_point2(self):   #Ввод 2 точки
        if tf:
            x1 = int(input("Введите х: "))
            y1 = int(input("Введите у: "))
            L = math.sqrt((self.__point1[0] - self.__point2[0])**2 + (self.__point1[0] - self.__point2[0])**2)
            print(f"Длина равна: {round(L,3)}")
            self.__point2[0] = x1
            self.__point2[1] = y1
            f = math.atan((y1 - self.__point1[1]) / (x1 - self.__point1[0]))
            self.__point1[0] = L * math.cos(f) + x1
            self.__point1[1] = L * math.sin(f) + y1

otrzok1 = Otrezok([1,2],[2,3])      #Создание 1 отрезка
print(f"{otrzok1.get_point1()} {otrzok1.get_point2()}")
otrzok2 = Otrezok([4,2],[4,3])      #Создание 2 отрезка
print(f"{otrzok2.get_point1()} {otrzok2.get_point2()}")
otrzok1.set_point1()        #Использование метода для изменения первой точки
print(f"{otrzok1.get_point1()} {otrzok1.get_point2()}")
otrzok1.set_point2()        #Использование метода для изменения второй точки
print(f"{otrzok1.get_point1()} {otrzok1.get_point2()}")