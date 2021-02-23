import random
import turtle
import time

score = 0
high_score = 0
delay = 0.05


s = turtle.Screen()
s.setup(width=1000, height=1000)
s.title("Snake Game")
s.tracer(0)

turtle.bgcolor("black")
turtle.color("orange")
turtle.shape("square")
turtle.speed(0)
turtle.penup()
turtle.goto(-400, 400)
turtle.pendown()
turtle.pensize(5)
turtle.fd(800)
turtle.rt(90)
turtle.fd(800)
turtle.rt(90)
turtle.fd(800)
turtle.rt(90)
turtle.fd(800)

sm = turtle.Turtle()
sm.shape('circle')
sm.fillcolor('blue')
sm.turtlesize(1.5)

snake = turtle.Turtle()
snake.speed(0)
snake.turtlesize(1)
snake.color("green")
snake.shape("circle")
snake.penup()
snake.goto(0, 0)
snake.direction = 'stop'

fruit = turtle.Turtle()
fruit.speed(0)
fruit.color("red")
fruit.turtlesize(1)
fruit.shape("circle")
fruit.penup()
fruit.goto(0, 100)

score_ = turtle.Turtle()
score_.speed(0)
score_.color("white")
score_.penup()
score_.hideturtle()
score_.goto(0, 400)
score_.write("Score : {} High Score: {}".format(score, high_score), align='center', font=('candara', 15, 'bold'))

segments = []

def go_up():
    snake.direction = 'up'


def go_down():
    snake.direction = 'down'


def go_right():
    snake.direction = 'right'


def go_left():
    snake.direction = 'left'


def move():
    if snake.direction == 'up':
        y = snake.ycor()
        snake.sety(y + 20)
    if snake.direction == 'down':
        y = snake.ycor()
        snake.sety(y - 20)
    if snake.direction == 'right':
        x = snake.xcor()
        snake.setx(x + 20)
    if snake.direction == 'left':
        x = snake.xcor()
        snake.setx(x - 20)


s.listen()
s.onkeypress(go_up, 'Up')
s.onkeypress(go_down, 'Down')
s.onkeypress(go_left, 'Left')
s.onkeypress(go_right, 'Right')

while True:
    s.update()
    if snake.xcor() > 400 or snake.xcor() < -400 or snake.ycor() < -400 or snake.ycor() > 400:
        time.sleep(1)
        snake.goto(0, 0)
        snake.direction = 'stop'

        score = 0
        score_.clear()
        score_.write("Score: {} High Score: {}".format(score, high_score),align='center',font=('candara',14,'bold'))

        for segment in segments:
            segment.goto(1000, 1000)

        segments.clear()

    if snake.distance(fruit) < 20:
        x = random.randint(0, 350)
        y = random.randint(0, 350)
        fruit.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('circle')
        new_segment.color('grey')
        new_segment.turtlesize(1)
        new_segment.penup()
        segments.append(new_segment)

        score += 10
        if high_score < score:
            high_score = score
        score_.clear()
        score_.write("Score: {} High Score: {}".format(score, high_score), align='center', font=('candara', 14, 'bold'))

    for i in range(len(segments)-1,0,-1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)

    if len(segments) > 0:
        x = snake.xcor()
        y = snake.ycor()
        segments[0].goto(x, y)

    move()

    for segment in segments:
        if segment.distance(snake) < 20:
            time.sleep(1)
            snake.goto(0, 0)
            snake.direction = 'stop'

            for segment in segments:
                segment.goto(1000, 1000)

            segments.clear()

            score_.clear()
            score_.write("Score: {} High Score: {}".format(score, high_score), align='center', font=('candara', 14, 'bold'))

    time.sleep(delay)

s.mainloop()
