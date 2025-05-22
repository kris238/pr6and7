from datetime import datetime
def dt(date):
    try:
        d = datetime.strptime(date, "%d.%m.%Y")
    except ValueError:
        return "Неверный формат даты. Используйте формат ДД.ММ.ГГГГ."
    try:
        new_date = d.strftime("%A, %d %B, %Y год")
        return new_date
    except Exception as a:
        return f"Oшибка: {str(a)}"
date = input("Введите дату (dd.mm.yyyy): ")
print(dt(date))
