class City:
    def __init__(self, name, country, language):
        self.name = name
        self.country = country
        self.language = language
    def inf(self):
        print(f"Информация о городе:\nНазвание: {self.name}\nСтрана: {self.country}\nЯзык: {self.language}")
class Obl(City):
    def __init__(self, name, country, language, obl):
        super().__init__(name, country, language)
        self.obl=obl
    def infobl(self):
        print(f"Область = {self.obl}")
City1 = City("Москва", "Россия", "Русский")
City1.inf()
City2 = Obl("Омск", "Россия", "Русский","Омская")
City2.inf()
City2.infobl()
