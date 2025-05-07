class Counter:
    def __init__(self, c=0):
        self.c = c
    def increase(self):
        self.c += 1
        print("Счетчик увеличен на 1.")
    def decrease(self):
        self.c -= 1
        print("Счетчик уменьшен на 1.")
    def c_v(self):
        return self.c
if __name__ == "__main__":
    counter = Counter()
    print("Текущее значение счетчика:", counter.c_v())
    counter.increase()
    print("Текущее значение счетчика:", counter.c_v())
    counter.decrease()
    print("Текущее значение счетчика:", counter.c_v())
    counter2 = Counter(4)
    print("Текущее значение счетчика с ПЗ:", counter2.c_v())
    counter2.increase()
    print("Текущее значение счетчика:", counter2.c_v())


