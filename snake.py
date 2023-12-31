"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import randrange
from turtle import *
import random

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
colors = ['blue', 'green', 'orange', 'purple', 'yellow']


def pickColors():       # función para elegir los colores de la serpiente y la comida
    snakeColor = colors[randrange(0, len(colors))]
    foodColor = colors[randrange(0, len(colors))]
    while snakeColor == foodColor:                      # la serpiente y la comida no pueden ser del mismo color
        foodColor = colors[randrange(0, len(colors))]
    return snakeColor, foodColor

  
def move_food():
    """Move food to a random position."""
    food.x = food.x + random.randrange(-1, 1) * 10
    food.y = food.y + random.randrange(-1, 1) * 10
    ontimer(move_food, 3000)


def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, snakeColor)   # se dibuja la serpiente con el color elegido

    square(food.x, food.y, 9, foodColor)    # se dibuja la comida con el color elegido
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
snakeColor, foodColor = pickColors()    # se eligen los colores de la serpiente y la comida
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
move_food()
done()
