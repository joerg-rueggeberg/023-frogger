from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.color("black")
        self.shape("turtle")
        self.setpos(STARTING_POSITION)
        self.setheading(90)

    def up(self):
        self.fd(MOVE_DISTANCE)

    def down(self):
        self.bk(MOVE_DISTANCE)

    def reset_pos(self):
        self.setpos(STARTING_POSITION)
