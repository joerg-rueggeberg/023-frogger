from random import randint, choice
from turtle import Turtle

COLORS = ["black", "LightSteelBlue1", "red3", "bisque4", "chocolate4", "DarkSeaGreen1"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_LENGTH = [2, 4]


class CarManager:
    def __init__(self):
        self.cars_r = []
        self.cars_l = []
        self.speed_l = STARTING_MOVE_DISTANCE
        self.speed_r = STARTING_MOVE_DISTANCE

    def spawn_r(self):
        spawn_chance_r = randint(1, 12)
        if spawn_chance_r == 1:
            car_r = Turtle()
            car_r.shape("square")
            car_r.color(choice(COLORS))
            car_r.seth(180)
            car_r.shapesize(1, 2)
            car_r.pu()
            car_r.setpos(300, randint(25, 225))
            self.cars_r.append(car_r)

    def spawn_l(self):
        spawn_chance_l = randint(1, 12)
        if spawn_chance_l == 1:
            car_l = Turtle()
            car_l.shape("square")
            car_l.color(choice(COLORS))
            car_l.seth(0)
            car_l.shapesize(1, 2)
            car_l.pu()
            car_l.setpos(-300, randint(-225, -25))
            self.cars_l.append(car_l)

    def move_r(self):
        for list_car in range(len(self.cars_r)):
            self.cars_r[list_car].fd(self.speed_r)

    def move_l(self):
        for list_car in range(len(self.cars_l)):
            self.cars_l[list_car].fd(self.speed_l)

    def level_up(self):
        self.speed_r += MOVE_INCREMENT
        self.speed_l += MOVE_INCREMENT
