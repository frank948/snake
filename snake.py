import random
import turtle
import time

score = 0
high_score = 0

def setup():

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

    snake = turtle.Turtle()
    snake.speed(1)
    snake.color("green")
    snake.pensize(5)
    snake.shape("square")
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
    score_.write("Score : 0 High Score: 0", align='center', font=('candara', 15, 'bold'))

    base = 0

    def move():
        #print('working')
        while base == -1:
            #print(base, "where am i")
            def left():
                x = snake.xcor()
                snake.setx(x - 10)
                #print((snake.xcor()), (snake.ycor()))
                #print(base)
                #print('left')
            left()
        while base == 1:
            #print(base, "where am i")
            def right():
                x = snake.xcor()
                snake.setx(x + 10)
                #print(base)
                #print('right')
            right()
        while base == -2:
            #print(base, "where am i")
            def down():
                y = snake.ycor()
                snake.sety(y - 10)
                #print(base)
                #print('down')
            down()
        while base == 2:
            #print(base, "where am i")
            def up():
                y = snake.ycor()
                snake.sety(y + 10)
                #print(base)
                #print('up')
            up()
        if base == 3:
            def stop():
                #time.sleep(1)
                snake.speed(1)
                s.done()
                print('done')
                print((snake.xcor()), (snake.ycor()))
            stop()
        if base == 4:
            def reset():
                snake.speed(0)
                setup()
                print('reset')
            reset()

    def go_left():
        global base
        base = -1
        #print(base, 'left')
        move()
        return base
    def go_right():
        global base
        base = 1
        #print(base, 'right')
        move()
        return base
    def go_down():
        global base
        base = -2
        #print(base, 'down')
        move()
        return base
    def go_up():
        global base
        base = 2
        #print(base, 'up')
        move()
        return base
    def stop_():
        global base
        base = 3
        move()
        return base
    def reset_():
        global base
        base = 4
        move()
        return base

    s.listen()
    s.onkeypress(go_up, 'Up')
    s.onkeypress(go_down, 'Down')
    s.onkeypress(go_left, 'Left')
    s.onkeypress(go_right, 'Right')
    s.onkeypress(stop_, 'w')
    s.onkeypress(reset_, 'e')

    s.update()
    if (snake.xcor() < -397):
        x = snake.xcor()
        y = snake.ycor()
        snake.goto(x, y)
        print(snake.position)

        #snake.goto(0, 0)
        #snake.direction = "stop"
        #score = 0
        #delay = 0.1
        #score_.clear()
        #score_.write("Score: {} High Score: {}".format(score, high_score), align='center', font=('candara', 14, 'bold'))
    '''
        if snake.distance(fruit) < 20:
            score += 1
            x = random.randint(-250, 250)
            y = random.randint(-250, 250)
            x_1 = snake.xcor()
            y_1 = snake.ycor()
            fruit.goto(x, y)
            c = snake.clone()
    '''
    move()
    s.mainloop()
setup()
