import time
from turtle import Screen
from street import Street
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Crossing Turtle (Frogger) - Sinclair")
screen.setup(width=600, height=600)
screen.tracer(0)


street = Street()
turtle = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

hello = screen.textinput("Crossing Turtle (Frogger) - Sinclair",
                         "Welcome to Crossing Turtle.\n\n"
                         "Your goal is to reach the other side of the street\n without gettin hit by a car.\n\n"
                         "Controls: ⬆/⬇ \n\nType 'start' to start.")

screen.listen()
screen.onkey(turtle.up, "Up")
screen.onkey(turtle.down, "Down")

game_over = False

while not game_over:
    car_manager.spawn_r()
    car_manager.spawn_l()
    time.sleep(0.1)
    screen.update()
    car_manager.move_r()
    car_manager.move_l()

    # crossed the street
    if turtle.ycor() > 250:
        turtle.reset_pos()
        scoreboard.level_up()
        car_manager.level_up()

    # collision with car
    for c in car_manager.cars_l:
        if turtle.distance(c) < 25:
            game_over = scoreboard.life_reduce()
            turtle.reset_pos()
    for c in car_manager.cars_r:
        if turtle.distance(c) < 25:
            game_over = scoreboard.life_reduce()
            turtle.reset_pos()

screen.exitonclick()
