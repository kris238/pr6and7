class Train:
    def __init__(self, destination, n_train, time):
        self.destination = destination
        self.n_train = n_train
        self.time = time
    def display_inf(self):
        print(f"Пункт назначения: {self.destination}")
        print(f"Номер поезда: {self.n_train}")
        print(f"Время отправления: {self.time}")
trains = [Train("Томск", "23", "13:10"), Train("Новосибирск", "24", "18:45")]
t = input("Введите номер поезда: ")
found = False
for train in trains:
    if train.n_train == t:
        print("Информация о поезде:")
        train.display_inf()
        found = True
        break
if not found:
    print("Поезд с таким номером не найден.")
