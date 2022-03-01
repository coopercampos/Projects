from turtle import Turtle


class Score:
    def __init__(self):
        self.writer = Turtle(visible=False)
        self.writer.penup()
        self.writer.goto(x=0, y=260)
        self.writer.pencolor("white")
        data = open("data.txt", "r")
        self.high_score = int(data.read())
        self.score = 0
        self.writer.write(arg=f"Current score: {self.score} High Score:{self.high_score}", align="center",
                          font=("Verdana", 15, "normal"))

    def new_score(self):
        self.writer.clear()
        self.score += 1
        if self.score > self.high_score:
            self.att_high_score()
        self.writer.goto(x=0, y=260)
        self.writer.write(arg=f"Current score:{self.score} High Score:{self.high_score}", align="center",
                          font=("Verdana", 15, "normal"))

    def att_high_score(self):
        new_high_score = self.score
        self.high_score = self.score
        with open("data.txt", "w") as data:
            data.write(f"{new_high_score}")

    def game_over(self):
        self.writer.goto(x=0, y=0)
        self.writer.write(arg=f"Game over.", align="center",
                          font=("Verdana", 15, "normal"))
