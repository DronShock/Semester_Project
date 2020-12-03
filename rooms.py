import Items_map


class Room(Item_map):
    l = (['00', '00', '15', '17', '19', '21', '23'],
         ['00', '00', '14', '16', '18', '20', '22'],
         ['00', '00', '03', '04', '05', '12', '13'],
         ['00', '01', '02', '00', '06', '07', '08'],
         ['00', '00', '00', '00', '09', '10', '11'])

    def __init__(self, number, *things):
        for i in things:

        self.number = number
        self.plot_pos = 1
        # не трогать plot_pos
        # TODO: привязать картинку к комнате

    def draw(self):
        pass


def create_rooms():
    pass
    # TODO: реализовать создание всех комнат через массив l
