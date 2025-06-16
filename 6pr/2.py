class User:
    def init(self, login, password):
        self.login = login
        self.password = password
Users = [
    User("user1", "pass1"),
    User("user2", "pass2"),
    User("user3", "pass3"),
    User("user4", "pass4"),
    User("user5", "pass5"),
]
login = input('Введите логин:')
password = input('Введите пароль:')
found_user = None
for user in Users:
    if user.login == login and user.password == password:
        found_user = user
        break
if found_user:
    print(f"Найден пользователь: Логин - {found_user.login}, Пароль - {found_user.password}")
else:
    print("Пользователь не найден.")