class Worker:
    def __init__(self, name, surname, rate, days):
        self.__name = name
        self.__surname = surname
        self.__rate = rate
        self.__days = days
    def GetSalary(self):
        salary = self.__rate * self.__days
        return salary
    def get_name(self):
        return self.__name
    def get_surname(self):
        return self.__surname
    def get_rate(self):
        return self.__rate
    def get_days(self):
        return self.__days
w = Worker("Кристина", "Мухамедзянова", 350, 30)
print(w.GetSalary())
