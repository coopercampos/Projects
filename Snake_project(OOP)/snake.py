from turtle import Turtle, Screen, colormode
import time
from food import Food
from score import Score
import random
COLORS = [(251, 240, 230), (228, 243, 237), (217, 226, 234), (69, 104, 128), (161, 80, 23), (136, 164, 182), (33, 126, 90), (246, 236, 244), (229, 147, 86), (31, 47, 62), (116, 191, 161), (39, 177, 128), (124, 65, 140),
          (15, 94, 71), (202, 151, 17), (242, 206, 91), (188, 138, 195), (137, 219, 189), (213, 83, 70), (124, 39, 29), (165, 95, 172), (89, 43, 97), (99, 37, 13), (234, 170, 164), (48, 61, 89), (214, 176, 213),
          (69, 33, 83), (111, 118, 165), (121, 83, 2), (240, 197, 9)]
T = [i for i in range(10, 255, 15)]
for i in range(255, 0, -5):
    T.append(i)


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.snake_body = []            # Setting the screen.
        self.screen = Screen()
        self.screen.tracer(0)
        self.screen.bgcolor("black")
        self.screen.setup(width=600, height=600)
        self.screen.title("Snake game")
        # Starting body
        x_position = 0
        for i in range(4):
            snake = Turtle()  # Make each part of the snake's body the way it should be.
            snake.shape("square")
            colormode(255)
            snake.color((255, T[0], T[0]))
            snake.penup()
            snake.goto(x_position, 0)
            self.snake_body.append(snake)
            x_position -= 20
            del(T[0])
        self.screen.update()
        self.head = self.snake_body[0]

    def move(self):
        """forward, backwards, right or left."""
        for i in range(len(self.snake_body) - 1, 0, -1):
            self.snake_body[i].goto(self.snake_body[i - 1].pos())
        self.snake_body[0].forward(20)
        self.screen.update()
        time.sleep(0.15)

    def forward_(self):
        if not self.snake_body[0].heading() == 270:
            self.snake_body[0].setheading(90)

    def backward_(self):
        if not self.snake_body[0].heading() == 90:
            self.snake_body[0].setheading(270)

    def right_(self):
        if not self.snake_body[0].heading() == 180:
            self.snake_body[0].setheading(0)

    def left_(self):
        if not self.snake_body[0].heading() == 0:
            self.snake_body[0].setheading(180)

    def game_on(self):
        score = Score()
        self.screen.listen()
        self.screen.onkey(fun=self.forward_, key="Up")
        self.screen.onkey(fun=self.backward_, key="Down")
        self.screen.onkey(fun=self.left_, key="Left")
        self.screen.onkey(fun=self.right_, key="Right")
        food = Food()
        while self.game_is_on():
            self.move()
            # Detect collision with food
            if self.head.distance(food) < 15:
                food.refresh()
                self.new_seg()
                score.new_score()
        score.game_over()

    def game_is_on(self):
        for part in self.snake_body[1:]:
            if self.head.distance(part) < 10:
                return False
        if self.head.xcor() > 270 or self.head.xcor() < -270:
            return False
        elif self.head.ycor() < -270 or self.head.ycor() > 270:
            return False
        else:
            return True

    def new_seg(self):
        snake = Turtle()  # Make each part of the snake's body the way it should be.
        snake.shape("square")
        snake.color((255, T[0], T[0]))
        snake.penup()
        last_part = len(self.snake_body) - 1
        x = self.snake_body[last_part].xcor()
        y = self.snake_body[last_part].xcor()
        del(T[0])
        if self.head.heading == 0:
            snake.goto(x-20, y)
        elif self.head.heading == 90:
            snake.goto(x, y-20)
        elif self.head.heading == 180:
            snake.goto(x+20, y)
        else:
            snake.goto(x, y+20)
        self.snake_body.append(snake)

    def exitonclick(self):
        self.screen.exitonclick()

    def update(self):
        self.screen.update()