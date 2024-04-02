class Tomato:
    states=["отсутствует", "цветение", "зеленый", "красный"]
    def __init__(self,index):
        self._index=index
        self._state=Tomato.states[0]
        #атрибуты экземпляра класса
    def grow(self):
        self._state=Tomato.states[(Tomato.states.index(self._state) + 1) % len(Tomato.states)]
    def is_ripe(self):
        return self._state == 'красный'
class TomatoBush:
    def __init__(self,kol):
        self.tomatoes = [Tomato(i) for i in range(kol)]
    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()
    def all_are_ripe(self):
        return all(tomato.is_ripe() for tomato in self.tomatoes)
    def give_away_all(self):
        self.tomatoes = []
class Gardener:
    def __init__(self,name,plant):
        self.name = name
        self._plant = plant
    def work(self):
        self._plant.grow_all()
        print(f'{self.name} работает')
    def harvest(self):
        if self._plant.all_are_ripe():
            print(f'Томаты красные. {self.name} собрал урожай.')
            self._plant.give_away_all()
        else:
            print('Томаты не красные')
    @staticmethod
    def knowledge_base():
        print('Справка по садоводству')
Gardener.knowledge_base()
tomato_bush = TomatoBush(int(input('Сколько томатов на кусте?: ')))
gardener = Gardener(input('Ваше имя: '), tomato_bush)

while len(tomato_bush.tomatoes) != 0:
    action = int(input('Выберите действие: 1 - работать с кустом; 2 - Попробовать собрать урожай: '))
    if action == 1:
        gardener.work()
    elif action == 2:
        gardener.harvest()
        print()
    else:
        print('Ошибка')


