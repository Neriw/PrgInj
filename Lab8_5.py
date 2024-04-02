class obj:
    def inf(self):
        pass
class City(obj):
    def __init__(self, name, country, language):
        self.name = name
        self.country = country
        self.language = language
    def inf(self):
        print(f"Информация о городе:\nНазвание: {self.name}\nСтрана: {self.country}\nЯзык: {self.language}")
class StreetIn(obj):
    def __init__(self, name, street):
        self.name=name
        self.street=street
    def inf(self):
        print(f"Город = {self.name}\nУлица = {self.street}")
City1 = City("Москва", "Россия", "Русский")
City1.inf()
City2 = StreetIn("Омск", "Ленина")
City2.inf()
