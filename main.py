class Otrezok:      #Объявление класса

    def __init__(self, point1, point2):     #
        self.__point1 = point1
        self.__point2 = point2

    def get_point1(self):
        return self.__point1

    def set_point1(self, point1):
        self.__point1 = point1

    def get_point2(self):
        return self.__point2

    def set_point2(self, point2):
        self.__point2 = point2

otrzok1 = Otrezok([1,2],[2,3])
print(f"{otrzok1.get_point1()} {otrzok1.get_point2()}")
otrzok2 = Otrezok([4,2],[4,3])
print(f"{otrzok2.get_point1()} {otrzok2.get_point2()}")