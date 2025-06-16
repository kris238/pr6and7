class FitnessCenter:
    def init(self, client_code, year, month, session_duration):
        self.client_code = client_code
        self.year = year
        self.month = month
        self.session_duration = session_duration
sessions = [
    FitnessCenter(1, 2025, 1, 60),
    FitnessCenter(2, 2025, 2, 45),
    FitnessCenter(3, 2025, 3, 75),
    FitnessCenter(4, 2025, 4, 30),
    FitnessCenter(5, 2025, 5, 90),
]
longest_session = max(sessions, key=lambda s: s.session_duration)
shortest_session = min(sessions, key=lambda s: s.session_duration)
print(f"Самое продолжительное занятие: Код клиента {longest_session.client_code}, "
      f"Год {longest_session.year}, Номер месяца {longest_session.month}, "
      f"Продолжительность занятия {longest_session.session_duration} минут.")
print(f"Самое короткое занятие: Код клиента {shortest_session.client_code}, "
      f"Год {shortest_session.year}, Номер месяца {shortest_session.month}, "
      f"Продолжительность занятия {shortest_session.session_duration} минут.")