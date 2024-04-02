class City:
    def __init__(self, name, country, language):
        self.name = name
        self.country = country
        self.language = language
    def inf(self):
        return f"Информация о городе:\nНазвание: {self.name}\nСтрана: {self.country}\nЯзык: {self.language}"

City1 = City("Москва", "Россия", "Русский")
print(City1.name)
print(City1.inf())
