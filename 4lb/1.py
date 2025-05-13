import sqlite3

def c_db(name='students.db'):
    con = sqlite3.connect(name)
    con.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                surname TEXT,
                patronymic TEXT,
                gr TEXT,
                grades TEXT
            )
        ''')
    return con
def add_student(con, name, surname, patronymic, gr, grades):
    c = con.cursor()
    c.execute('''
        INSERT INTO students (name, surname, patronymic, gr, grades)
        VALUES (?, ?, ?, ?, ?)
    ''', (name, surname, patronymic, gr, ','.join(map(str, grades))))
    con.commit()
def all_students(con):
    c = con.cursor()
    c.execute('SELECT * FROM students')
    return c.fetchall()
def one_student(con, id):
    c = con.cursor()
    c.execute('SELECT * FROM students WHERE id=?', (id,))
    return c.fetchone()
def edit(con, id, name, surname, patronymic, gr, grades):
    c = con.cursor()
    c.execute('''
        UPDATE students SET name=?, surname=?, patronymic=?, gr=?, grades=?
        WHERE id=?
    ''', (name, surname, patronymic, gr, ','.join(map(str, grades)), id))
    con.commit()
def delete(con, id):
    c = con.cursor()
    c.execute('DELETE FROM students WHERE id=?', (id,))
    con.commit()
def GP_group(con, gr):
    c = con.cursor()
    c.execute('SELECT grades FROM students WHERE gr=?', (gr,))
    grades = []
    for el in c:
        grades.extend(map(int, el[0].split(',')))
    return sum(grades) / len(grades) if grades else 0
def main():
    con = c_db()
    while True:
        a = input('\n'
                  '1 - Добавление нового студента\n'
                  '2 - Просмотр всех студентов\n'
                  '3 - Просмотр одного студента с средним баллом\n'
                  '4 - Редактирование студента\n'
                  '5 - Удаление студента\n'
                  '6 - Просмотр среднего балла студентов группы\n')
        if a == '1':
            name = input("Введите имя:")
            surname = input("Введите фамилию:")
            patronymic = input("Введите отчество:")
            gr = input("Введите группу:")
            grades = input("Введите оценки (через запятую):")
            gradess = list(map(int, grades.split(',')))
            add_student(con, name, surname, patronymic, gr, gradess)
        elif a == '2':
            students = all_students(con)
            print(students)
        elif a == '3':
            students = one_student(con, id)
            print(students)
        elif a == '4':
            id = int(input("Введите ID студента для редактирования: "))
            name = input("Введите имя: ")
            surname = input("Введите фамилию:")
            patronymic = input("Введите отчество:")
            gr = input("Введите группу:")
            grades = input("Введите оценки (через запятую):")
            gradess = list(map(int, grades.split(',')))
            edit(con, id, name, surname, patronymic, gr, gradess)
        elif a == '5':
            id = int(input("Введите ID студента для удаления: "))
            delete(con, id)
        elif a == '6':
            gr = input("Введите название группы для расчета среднего балла: ")
            av = GP_group(con, gr)
            print(av)
        else:
            break
    con.close()
if __name__ == "__main__":
    main()
