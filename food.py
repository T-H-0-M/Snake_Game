"""
food.py: A module containing the Food class for the Snake game.

The Food class represents the food item that the snake needs to eat in order to grow. It inherits from the Turtle class
in the turtle module and provides methods for initializing and refreshing the position of the food item.

"""

from turtle import Turtle
import random


class Food(Turtle):
    """
    A class representing the food item in the Snake game.

    Attributes:
        - shape (str): The shape of the food item (circle).
        - color (str): The color of the food item (red).

    Methods:
        - __init__(): Initializes a new instance of the Food class.
        - refresh(): Refreshes the position of the food item.

    """

    def __init__(self):
        """
        Initializes a new instance of the Food class.

        The food item is represented as a circle and is initially placed at a random position on the screen.
        The size of the food item is adjusted using the shapesize method of the Turtle class.

        """
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """
        Refreshes the position of the food item.

        Generates random x and y coordinates within the game screen boundaries and moves the food item to that position.

        """
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        self.setpos(rand_x, rand_y)
