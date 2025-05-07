class Worker:
    def __init__(self, name, surname, rate, days):
        self.name = name
        self.surname = surname
        self.rate = rate
        self.days = days
    def GetSalary(self):
        salary = self.rate * self.days
        return salary
worker = Worker("Кристина", "Мухамедзянова", 350, 30)
print(worker.GetSalary())
