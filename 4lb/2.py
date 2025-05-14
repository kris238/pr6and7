import sqlite3
def cr_tab():
    con = sqlite3.connect('i_love_drink.db')
    c = con.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS drinks (
        id INTEGER PRIMARY KEY,
        name TEXT,
        strength REAL,
        volume REAL,
        price REAL
    )
    ''')
    c.execute('''
    CREATE TABLE IF NOT EXISTS cocktails (
        id INTEGER PRIMARY KEY,
        name TEXT,
        strength REAL,
        ingredients TEXT,
        price REAL
    )
    ''')
    return con
def add_drink(con):
    cursor = con.cursor()
    name = input("Введите название алкогольного напитка:")
    strength = float(input("Введите крепость:"))
    volume = float(input("Введите объем(л):"))
    price = float(input("Введите цену:"))
    cursor.execute('''
    INSERT INTO drinks (name, strength, volume, price)
    VALUES (?, ?, ?, ?)
    ''', (name, strength, volume, price))
    con.commit()
    print("Напиток успешно добавлен))")
def add_cocktail(con):
    c = con.cursor()
    name = input("Введите название коктейля:")
    ingredients = input("Введите состав коктейля(через запятую):")
    price = float(input("Введите цену:"))
    s = [c.execute('SELECT strength FROM drinks WHERE name = ?', (ing.strip(),)).fetchone()[0] for ing in
                ingredients.split(',')]
    strength = sum(s) / len(s) if s else 0
    c.execute('''
    INSERT INTO cocktails (name, strength, ingredients, price)
    VALUES (?, ?, ?, ?)
    ''', (name, strength, ingredients, price))
    con.commit()
    print("Коктейль успешно добавлен))")
def sale_drink(con):
    c = con.cursor()
    dr_name = input("Введите название:")
    quantity = int(input("Введите количество:"))
    c.execute('SELECT price, volume FROM drinks WHERE name = ?', (dr_name,))
    r = c.fetchone()
    if r:
        price, volume = r
        total_price = price * quantity
        print(f"Продажа {quantity} бутылок {dr_name} на сумму {total_price:.2f} руб")
    else:
        print("Опа, такого напитка нет")
def stock(con):
    c = con.cursor()
    dr_name = input("Введите название напитка чтобы пополнить запасы:")
    quantity = int(input("Введите количество:"))
    c.execute('SELECT name FROM drinks WHERE name = ?', (dr_name,))
    r = c.fetchone()
    if r:
        print("Запасы пополнены")
    else:
        print("Такого напитка ещё нет в наличии")
def main():
    con = cr_tab()
    while True:
        a = input("\n"
        "1 - Добавить напиток\n"
        "2 - Добавить коктейль\n"
        "3 - Продать напиток\n"
        "4 - Пополнить запасы\n")
        if a == "1":
            add_drink(con)
        elif a == "2":
            add_cocktail(con)
        elif a == "3":
            sale_drink(con)
        elif a == "4":
            stock(con)
        else:
            break
    con.close()
if __name__ == "__main__":
    main()