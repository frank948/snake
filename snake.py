import random
import turtle
import time

score = 1
high_score = 2

s = turtle.Screen()
s.setup(width=1000, height=1000)
s.title("Snake Game")


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
snake.speed(1)
snake.color("green")
snake.turtlesize(1)
snake.shape("circle")
snake.penup()
snake.goto(0, 0)

fruit = turtle.Turtle()
fruit.speed(0)
fruit.color("red")
fruit.pensize(5)
fruit.shape("circle")
fruit.penup()
fruit.goto(0, 100)

score_ = turtle.Turtle()
score_.color("white")
score_.penup()
score_.hideturtle()
score_.goto(0, 400)
score_.write("Score : {} High Score: {}".format(score, high_score), align='center', font=('candara', 15, 'bold'))

commands = turtle.Turtle()
commands.color("white")
commands.penup()
commands.hideturtle()
commands.goto(-400, 450)
commands.write("\'w\' to reset snake\n\'e\' to close window\narrows keys to move snake", align='left', font=('candara', 10, 'bold'))

base = 0


def move():

    while base == 3:
        time.sleep(1)
        snake.goto(0, 0)

    # print('working')

    while base == -1:
        # print(base, "where am i")
        def left():
            x = snake.xcor()
            snake.setx(x - 10)
            if snake.distance(fruit) < 20:
                x = random.randint(0, 200)
                y = random.randint(0, 200)
                fruit.goto(x, y)
            # print((snake.xcor()), (snake.ycor()))
            # print(base)
            # print('left')
        left()
    while base == 1:
        # print(base, "where am i")
        def right():
            x = snake.xcor()
            snake.setx(x + 10)
            if snake.distance(fruit) < 20:
                x = random.randint(0, 200)
                y = random.randint(0, 200)
                fruit.goto(x, y)
            # print(base)
            # print((snake.xcor()), (snake.ycor()))
            # print('right')
        right()
    while base == -2:
        # print(base, "where am i")
        def down():
            y = snake.ycor()
            snake.sety(y - 10)
            if snake.distance(fruit) < 20:
                x = random.randint(0, 200)
                y = random.randint(0, 200)
                fruit.goto(x, y)

            # print(base)
            # print((snake.xcor()), (snake.ycor()))
            # print('down')
        down()
    while base == 2:
        # print(base, "where am i")
        def up():
            y = snake.ycor()
            snake.sety(y + 10)
            if snake.distance(fruit) < 20:
                x = random.randint(0, 200)
                y = random.randint(0, 200)
                fruit.goto(x, y)
            # print(base)
            # print((snake.xcor()), (snake.ycor()))
            # print('up')
        up()

def go_left():
    global base
    base = -1
    # print(base, 'left')
    move()

def go_right():
    global base
    base = 1
    # print(base, 'right')
    move()

def go_down():
    global base
    base = -2
    # print(base, 'down')
    move()

def go_up():
    global base
    base = 2
    # print(base, 'up')
    move()

def reset_():
    global base
    base = 3
    move()

def done_():
    s.bye()


s.listen()
s.onkeypress(go_up, 'Up')
s.onkeypress(go_down, 'Down')
s.onkeypress(go_left, 'Left')
s.onkeypress(go_right, 'Right')
s.onkeypress(reset_, 'w')
s.onkeypress(done_, 'e')



s.update()
print('where is this')
if (snake.xcor() < -397):
    print('lose')

if snake.distance(fruit) < 50:
    print('where')


move()

s.mainloop()
