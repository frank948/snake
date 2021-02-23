import random
import turtle
import time

score = 0
high_score = 5
delay = 0.1

s = turtle.Screen()
s.setup(width=1000, height=1000)
s.title("Snake Game")
#s.tracer(0)

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
snake.color("green")
snake.turtlesize(1)
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


def go_up():
    if snake.direction != 'Down':
        snake.direction = 'Up'
        print('what')
def go_down():
    if snake.direction != 'Up':
        snake.direction = 'Down'

def go_right():
    if snake.direction != 'Left':
        snake.direction = 'Right'

def go_left():
    if snake.direction != 'Right':
        snake.direction = 'Left'

def move():
    if snake.direction == 'Up':
        y = snake.ycor()
        snake.sety(y + 15)
    if snake.direction == 'Down':
        y = snake.ycor()
        snake.sety(y - 15)
    if snake.direction == 'Right':
        x = snake.xcor()
        snake.setx(x + 15)
    if snake.direction == 'Left':
        x = snake.xcor()
        snake.setx(x - 15)


s.listen()
s.onkeypress(go_up, 'w')
s.onkeypress(go_down, 's')
s.onkeypress(go_left, 'a')
s.onkeypress(go_right, 'd')


move()


s.mainloop()
