class Car:

    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        print(f'создана машина: {self.name}, цвет - {self.color}, машина полицейская - {self.is_police}')

    def go(self):
        print(f'{self.name}: машина поехала')

    def stop(self):
        print(f'{self.name}: машина остановилась')

    def turn(self, direction):
        print(f"{self.name}: машина повернула {'налево' if direction == 0 else 'направо'}")

    def show_speed(self):
        print(f'{self.name}: скорость автомобиля = {self.speed}')


class WorkCar(Car):

    def show_speed(self):
        return f'{self.name}: Скорость автомобиля - {self.speed} - превышение скорости!' \
            if self.speed > 40 else f'{self.name}: скорость автомобиля - {self.speed}'


class TownCar(Car):

    def show_speed(self):
        return f'{self.name}: Скорость автомобиля - {self.speed} - превышение скорости!' \
            if self.speed > 60 else f'{self.name}: скорость автомобиля - {self.speed}'


class SportCar(Car):

    def show_speed(self):
        return f'{self.name}: Скорость автомобиля - {self.speed} - превышение скорости!' \
            if self.speed > 60 else f'{self.name}: скорость автомобиля - {self.speed}'


class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)


sport_car_1 = SportCar('Ferrari', 'красный', 250)
sport_car_1.turn('направо')

work_car_1 = TownCar('ЗИЛ', 'зеленый', 70)
work_car_1.show_speed()

police_car_1 = PoliceCar('Renault', 'белый', 80)
police_car_1.stop()

town_car_1 = TownCar('Hyundai', 'желтый', 100)
town_car_1.show_speed()

# почему-то не работает метод show_speed
