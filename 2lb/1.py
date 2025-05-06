class Student:
    def __init__(self, last_name, birth_date, group_number, grades):
        self.last_name = last_name
        self.birth_date = birth_date
        self.group_number = group_number
        self.grades = grades
    def display_info(self):
        print(f"Фамилия: {self.last_name}")
        print(f"Дата рождения: {self.birth_date}")
        print(f"Номер группы: {self.group_number}")
        print(f"Успеваемость: {self.grades}")
def main():
    student = Student("Русинова", "2008-07-12", "Группа 942", [4, 2, 3, 2, 5])
    search_last_name = input("Введите фамилию студента: ")
    search_birth_date = input("Введите дату рождения студента (ГГГГ-ММ-ДД): ")
    if search_last_name == student.last_name and search_birth_date == student.birth_date:
        print("Студент найден:")
        student.display_info()
    else:
        print("Студент не найден.")
if __name__ == "__main__":
    main()