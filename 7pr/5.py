class FitnessCenter:
    def init(self, client_code, year, month, session_duration):
        self.client_code = client_code
        self.year = year
        self.month = month
        self.session_duration = session_duration
sessions = [
    FitnessCenter(1, 2023, 1, 60),
    FitnessCenter(2, 2022, 2, 45),
    FitnessCenter(3, 2023, 3, 75),
    FitnessCenter(4, 2021, 4, 30),
    FitnessCenter(5, 2022, 5, 90),
    FitnessCenter(6, 2021, 6, 120),
    FitnessCenter(7, 2023, 7, 45),
    FitnessCenter(8, 2023, 8, 30),
    FitnessCenter(9, 2022, 9, 60),
    FitnessCenter(10, 2021, 10, 15),
]
yearly_durations = {}
for session in sessions:
    if session.year not in yearly_durations:
        yearly_durations[session.year] = 0
    yearly_durations[session.year] += session.session_duration
max_year = None
max_duration = 0
for year, duration in yearly_durations.items():
    if duration > max_duration or (duration == max_duration and (max_year is None or year < max_year)):
        max_duration = duration
        max_year = year
print(f"Год с наибольшей суммарной продолжительностью занятий: {max_year}, "
      f"суммарная продолжительность: {max_duration} минут.")