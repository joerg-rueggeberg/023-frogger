from turtle import Turtle
FONT = ("Verdana", 12, "bold")
FONT_T = ("Verdana", 20, "bold")
POSITION = (-280, 265)
POSITION_L = (160, 265, )


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.life = 2
        self.level = 1
        self.pu()
        self.hideturtle()
        self.setpos(POSITION)
        self.write(f"Level: {self.level}", align="left", font=FONT)
        self.setpos(POSITION_L)
        self.write(f"Turtles left: {self.life}", align="left", font=FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.setpos(POSITION)
        self.write(f"Level: {self.level}", align="left", font=FONT)
        self.setpos(POSITION_L)
        self.write(f"Turtles left: {self.life}", align="left", font=FONT)

    def life_reduce(self):
        if self.life == 0:
            self.setpos(0, 0)
            self.write("GAME OVER!", align="center", font=FONT_T)
            return True
        else:
            self.life -= 1
            self.clear()
            self.setpos(POSITION)
            self.write(f"Level: {self.level}", align="left", font=FONT)
            self.setpos(POSITION_L)
            self.write(f"Turtles left: {self.life}", align="left", font=FONT)
