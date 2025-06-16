class Task:
    def init(self, date_start, date_finish, description):
        self.date_start = date_start
        self.date_finish = date_finish
        self.description = description
tasks = [
    Task("2025-10-01", "2025-10-05", "Занятие 1"),
    Task("2025-10-02", "2025-10-10", "Занятие 2"),
    Task("2025-10-03", "2025-10-15", "Занятие 3"),
    Task("2025-10-04", "2025-10-12", "Занятие 4"),
    Task("2025-10-05", "2025-10-20", "Занятие 5"),
]
latest_task = None
for task in tasks:
    if latest_task is None or task.date_finish > latest_task.date_finish:
        latest_task = task
if latest_task:
    print(f"Занятие, заканчивающееся позже всех: {latest_task.description}, "
          f"Дата начала - {latest_task.date_start}, "
          f"Дата окончания - {latest_task.date_finish}")
else:
    print("Список занятий пуст.")