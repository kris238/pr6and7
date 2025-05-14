import psutil
import sqlite3
from datetime import datetime
def cr_db():
    con = sqlite3.connect('system_monitor.db')
    c = con.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS monitoring (
            id INTEGER PRIMARY KEY,
            timestamp TEXT NOT NULL,
            cpu_usage REAL NOT NULL,
            m_usage REAL NOT NULL,
            d_usage REAL NOT NULL
        )
    ''')
    return con
def conduct_m(con):
    cpu_usage = psutil.cpu_percent(interval=1)
    m_inf = psutil.virtual_memory()
    m_usage = m_inf.percent
    d_inf = psutil.disk_usage('/')
    d_usage = d_inf.percent
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    c = con.cursor()
    c.execute('''
        INSERT INTO monitoring (timestamp, cpu_usage, m_usage, d_usage)
        VALUES (?, ?, ?, ?)
    ''', (timestamp, cpu_usage, m_usage, d_usage))
    con.commit()
def look_data(con):
    c = con.cursor()
    c.execute('SELECT * FROM monitoring')
    data = c.fetchall()
    for i in data:
        print(f"ID: {i[0]}, Time: {i[1]}, CPU: {i[2]}%, Memory: {i[3]}%, Disk: {i[4]}%")
def main():
    con = cr_db()
    while True:
        a = input("\n"
        "1. Провести мониторинг\n"
        "2. Показать сохраненные данные")
        if a == '1':
            conduct_m(con)
            print("Мониторинг проведен")
        elif a == '2':
            look_data(con)
        else:
            break
    con.close()
if __name__ == '__main__':
    main()


