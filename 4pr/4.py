from datetime import datetime
def dt(date):
    d = datetime.strptime(date, "%d.%m.%Y")
    new_date = d.strftime("%A, %d %B, %Y год")
    return new_date
date = input("Введите дату(dd-mm-yyyy):")
print(dt(date))