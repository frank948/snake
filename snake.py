import random
import turtle
import time

score = 0
high_score = 5

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
fruit.turtlesize(1)
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

    while base == 0:
        time.sleep(1)
        snake.goto(0, 0)
    while base == 3:
        global score
        score = 0
        score_.clear()
        score_.write("Score : {} High Score: {}".format(score, high_score), align='center',
                     font=('candara', 15, 'bold'))
        time.sleep(1)
        snake.goto(0, 0)

    while base == -1:
        def left():
            x = snake.xcor()
            snake.setx(x - 10)
            global score
            global high_score
            if snake.distance(fruit) < 20:
                x = random.randint(0, 350)
                y = random.randint(0, 350)
                fruit.goto(x, y)


                score += 1
                score_.clear()
                score_.write("Score : {} High Score: {}".format(score, high_score), align='center',
                             font=('candara', 15, 'bold'))
                if score > high_score:
                    high_score = score
                    print(high_score)
                    score_.clear()
                    score_.write("Score : {} High Score: {}".format(score, high_score), align='center',
                                 font=('candara', 15, 'bold'))
            if snake.xcor() < -400 or snake.xcor() > 400 or snake.ycor() < -400 or snake.ycor() > 400:
                score = 0
                score_.clear()
                score_.write("Score : {} High Score: {}".format(score, high_score), align='center',
                             font=('candara', 15, 'bold'))
                time.sleep(1)
                snake.goto(0, 0)
                global base
                base = 0
                return base


        left()
    while base == 1:
        # print(base, "where am i")
        def right():
            x = snake.xcor()
            snake.setx(x + 10)
            global score
            global high_score
            if snake.distance(fruit) < 20:
                x = random.randint(0, 350)
                y = random.randint(0, 350)
                fruit.goto(x, y)


                score += 1
                score_.clear()
                score_.write("Score : {} High Score: {}".format(score, high_score), align='center',
                             font=('candara', 15, 'bold'))
                if score > high_score:
                    high_score = score
                    print(high_score)
                    score_.clear()
                    score_.write("Score : {} High Score: {}".format(score, high_score), align='center',
                                 font=('candara', 15, 'bold'))
            if snake.xcor() < -400 or snake.xcor() > 400 or snake.ycor() < -400 or snake.ycor() > 400:
                score = 0
                score_.clear()
                score_.write("Score : {} High Score: {}".format(score, high_score), align='center',
                             font=('candara', 15, 'bold'))
                time.sleep(1)
                snake.goto(0, 0)
                global base
                base = 0
                return base

        right()
    while base == -2:
        def down():
            y = snake.ycor()
            snake.sety(y - 10)
            global score
            global high_score
            if snake.distance(fruit) < 20:
                x = random.randint(0, 350)
                y = random.randint(0, 350)
                fruit.goto(x, y)


                score += 1
                score_.clear()
                score_.write("Score : {} High Score: {}".format(score, high_score), align='center',
                             font=('candara', 15, 'bold'))
                if score > high_score:
                    high_score = score
                    print(high_score)
                    score_.clear()
                    score_.write("Score : {} High Score: {}".format(score, high_score), align='center',
                                 font=('candara', 15, 'bold'))
            if snake.xcor() < -400 or snake.xcor() > 400 or snake.ycor() < -400 or snake.ycor() > 400:
                score = 0
                score_.clear()
                score_.write("Score : {} High Score: {}".format(score, high_score), align='center',
                             font=('candara', 15, 'bold'))
                time.sleep(1)
                snake.goto(0, 0)
                global base
                base = 0
                return base

        down()
    while base == 2:
        def up():
            y = snake.ycor()
            snake.sety(y + 10)
            global score
            global high_score
            if snake.distance(fruit) < 20:
                x = random.randint(0, 350)
                y = random.randint(0, 350)
                fruit.goto(x, y)
                
                score += 1
                score_.clear()
                score_.write("Score : {} High Score: {}".format(score, high_score), align='center',
                             font=('candara', 15, 'bold'))
                if score > high_score:
                    high_score = score
                    print(high_score)
                    score_.clear()
                    score_.write("Score : {} High Score: {}".format(score, high_score), align='center',
                                     font=('candara', 15, 'bold'))
            if snake.xcor() < -400 or snake.xcor() > 400 or snake.ycor() < -400 or snake.ycor() > 400:
                score = 0
                score_.clear()
                score_.write("Score : {} High Score: {}".format(score, high_score), align='center',
                             font=('candara', 15, 'bold'))
                time.sleep(1)
                snake.goto(0, 0)
                global base
                base = 0
                return base
        up()
def go_left():
    global base
    base = -1
    move()
def go_right():
    global base
    base = 1
    move()
def go_down():
    global base
    base = -2
    move()

def go_up():
    global base
    base = 2
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

if (snake.xcor() < -397):
    print('lose')
move()
s.mainloop()
