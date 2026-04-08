import turtle
import time
import random

turtleWon = ""

turtle.tracer(0)
turtle.bgcolor("black")
finishLine = turtle.Turtle()
turtleOne = turtle.Turtle()
turtleTwo = turtle.Turtle()
turtleThree = turtle.Turtle()

turtles_list = [ turtleOne, turtleTwo, turtleThree ]

turtleOne.color("red")
turtleTwo.color("green")
turtleThree.color("yellow")
finishLine.color("purple")
finishLine.hideturtle()

turtleOne.penup()
turtleTwo.penup()
turtleThree.penup()
finishLine.penup()

finishLine.pensize(7)
finishLine.goto(700,900)
finishLine.pendown()
finishLine.goto(700,-900)

for turtles in turtles_list:
    turtles.shape("turtle")
    turtles.shapesize(5)

def turtles_moveBack():
    for turtles in turtles_list:
        while (turtles.xcor() > -500):
            turtles.back(10)
            time.sleep(0.01)
            turtle.update()

        if turtles == turtleOne:
            while (turtleOne.heading() < 90):
                turtleOne.left(1)
                time.sleep(0.001)
                turtle.update()

            while (turtleOne.ycor() < 500):
                turtleOne.forward(2)
                time.sleep(0.001)
                turtle.update()

            while (turtleOne.heading() > 0):
                turtleOne.right(1)
                time.sleep(0.001)
                turtle.update()

        if turtles == turtleThree:
            while (turtleThree.heading() != 270):
                turtleThree.right(1)
                time.sleep(0.001)
                turtle.update()

            while (turtleThree.ycor() > -500):
                turtleThree.forward(2)
                time.sleep(0.001)
                turtle.update()

            while (turtleThree.heading() != 0):
                turtleThree.left(1)
                time.sleep(0.001)
                turtle.update()

def main_loop():
    gameOver = False
    while not gameOver:
        for turtles in turtles_list:
            turtles.forward(random.randint(1,30))
            time.sleep(0.001)
            turtle.update()
            if turtleOne.xcor() > 700 or turtleTwo.xcor() > 700 or turtleThree.xcor() > 700:
                gameOver = True
                break

def gameOver():
    global turtleWon
    positions = [ turtleOne.xcor(), turtleTwo.xcor(), turtleThree.xcor() ]
    match positions.index(max(positions)):
        case 0:
            turtleWon = "red turtle"
        case 1:
            turtleWon = "green turtle"
        case 2:
            turtleWon = "yellow turtle"
    print(f"Game over, {turtleWon} won.")

def main():
    turtles_moveBack()
    main_loop()
    gameOver()
    turtle.done()

if __name__ == "__main__":
    main()