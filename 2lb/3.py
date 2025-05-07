class Numbers:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def display(self):
        print(f"Числа:{self.num1}, {self.num2}")
    def change(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        print("Числа изменен")
    def sum(self):
        return self.num1 + self.num2
    def max_n(self):
        return max(self.num1, self.num2)
numbers = Numbers(1, 4)
numbers.display()
numbers.change(3, 2)
numbers.display()
print("Сумма:", numbers.sum())
print("Наибольшее число:", numbers.max_n())
