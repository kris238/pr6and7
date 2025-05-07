class Class:
    def __init__(self, p1=0, p2=0):
        self.p1 = p1
        self.p2 = p2
    def __del__(self):
        print("Объект удален")
    def display(self):
        print(f"Св-о1: {self.p1}, св-о2: {self.p2}")
if __name__ == "__main__":
    a = Class()
    a.display()
    a1 = Class(4, 6)
    a1.display()
    del a
    del a1
