from turtle import Turtle
import random as rd


class Food(Turtle): #import all attributes and methods of turtle modules
    def __init__(self, x, y):
        super().__init__() #initializes the super module
        self.penup()
        self.shape('circle')
        self.color('red')
        self.x = x
        self.y = y
        self.speed(0)
        self.food_placement()
        
    def food_placement(self):
        """sets food to a random location"""
        self.penup()
        food_x = self.x-20
        food_y = self.y-20
        self.goto(rd.randint(int(-food_x), int(food_x)), rd.randint(int(-food_y), int(food_y)))