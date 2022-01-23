from turtle import Turtle
BOTTOM = [(-300, -250), (300, -250)]
TOP = [(-300, 250), (300, 250)]


class Street(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pencolor("DarkGrey")
        self.pu()
        self.pensize(50)
        self.setpos(-300, -275)
        self.pd()
        self.setpos(300, -275)
        self.pu()
        self.setpos(-300, 275)
        self.pd()
        self.setpos(300, 275)
        self.pu()
        self.pensize(1)
        self.color("black")
        self.setpos(BOTTOM[0])
        self.pd()
        self.setpos(BOTTOM[1])
        self.pu()
        self.setpos(TOP[0])
        self.pd()
        self.setpos(TOP[1])
        self.pu()
        self.pensize(3)
        self.setpos(-278, 0)
        for i in range(10):
            self.pd()
            self.fd(50)
            self.pu()
            self.fd(50)
