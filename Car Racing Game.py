import turtle
import random
import time

# Set up the screen
screen = turtle.Screen()
screen.title("Car Racing Game")
screen.bgcolor("#abcdef")
screen.setup(width=1080, height=720)
screen.tracer(0)

# Car
car = turtle.Turtle()
car.shape("square")
car.color("black")
car.penup()
car.goto(0, -250)
car.setheading(90)
car.speed(0)

# Enemy Car
enemy = turtle.Turtle()
enemy.shape("square")
enemy.color("black")
enemy.penup()
enemy.goto(random.randint(-350, 350), 250)
enemy.setheading(270)
enemy.speed(10)

# Movement
car_speed = 100

def move_left():
    x = car.xcor()
    if x > -350:
        x -= car_speed
    car.setx(x)

def move_right():
    x = car.xcor()
    if x < 350:
        x += car_speed
    car.setx(x)
def up():
    y = car.ycor()
    if y < 250:
        y += car_speed
    car.sety(y)
def down():
    y = car.ycor()
    if y > -250:
        y -= car_speed
    car.sety(y)

# Keyboard bindings
screen.listen()
screen.onkeypress(move_left, "a")
screen.onkeypress(move_right, "d")
screen.onkeypress(up, "w")
screen.onkeypress(down, "s")
# Main game loop
while True:
    screen.update()

    # Move enemy car down
    enemy.sety(enemy.ycor() - enemy.speed())

    # Check collision with the car
    if car.distance(enemy) < 30:
        car.color("red")
        screen.update()
        time.sleep(2)
        break

    # Reset enemy car position
    if enemy.ycor() < -300:
        enemy.goto(random.randint(-350, 350), 250)
    time.sleep(0.0001)

screen.mainloop()
