class City:
    def __init__(self, name, country, language):
        self.name = name
        self.country = country
        self.language = language

    def inf(self):
        print(f"Информация о городе:\nНазвание: {self.name}\nСтрана: {self.country}\nЯзык: {self.language}")
    def clear(self):
        self.name=""
        self.country=""
        self.language=""
City1 = City('Москва', "Россия", 'Русский')
City1.inf()
City1.clear()
City1.inf()