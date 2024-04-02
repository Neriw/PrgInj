class City:
    def __init__(self, name, country, language):
        self.name = name
        self.country = country
        self.language = language

    def inf(self):
        print(f"Информация о городе:\nНазвание: {self.name}\nСтрана: {self.country}\nЯзык: {self.language}")

City1 = City('Москва', "Россия", 'Русский')
City2 = City("Берлин", "Германия", "Немецкий")
City3 = City("Париж", "Франци", "Французксий")
City1.inf()
City2.inf()
City3.inf()