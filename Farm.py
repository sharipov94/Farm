## Проект создан
class Potato:       #Класс описывающий картошку
    def __init__(self, potato_id):
        self.potato_id = potato_id   #Номер картошки в грядке.
        self.growth_stage = 0    #Стадию зрелости (всего 4 стадии: 0 — посажена, 1 — росток, 2 — цветёт, 3 — созрела).

    def status_grow(self):      #Красивый вывод информации.
        if self.growth_stage == 0:
            return f"посажена"
        elif self.growth_stage == 1:
            return f"росток"
        elif self.growth_stage == 2:
            return f"цветёт"
        elif self.growth_stage == 3:
            return f"созрела"
        else:
            return "Что то пошло не так."

    def is_ripe(self):      #Проверяем созрела картошки.
        return self.growth_stage == 3   #вернёт True, если картошка созрела

    def grow(self):     #увеличивает стадию зрелости, если она ещё не максимальная.
        if self.growth_stage < 3:
            self.growth_stage += 1
            return f"Картошка {self.potato_id} перешла в стадию: {self.status_grow()}"
        else:
            return f"Картошка уже зрелая, пора собирать!"

    def status(self):       #возвращает текущее состояние картошки.
        return f"Картошка {self.potato_id} сейчас в стадии: {self.status_grow()}"

