class Stationery:

    def __init__(self, title='ErichKrause'):
        self.title = title

    def draw(self):
        print(f'Do you like drawing? {self.title}')


class Pen(Stationery):
    def draw(self):
        print(f'If you want to write a letter, take a pen! {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'If you want to keep it black and white, take a pencil! {self.title}')


class Highlighter(Stationery):
    def draw(self):
        print(f'If you want to make it colored, take a highlighter! {self.title}')


stationery_0 = Stationery()
pen_1 = Pen()
pencil_1 = Pencil()
highlighter_blue = Highlighter()

stationery_0.draw()
pen_1.draw()
pencil_1.draw()
highlighter_blue.draw()
