import turtle


#shows all three x positions of 3 first turtles
snake_position = [0, -20, -40]

class Snake:

    def __init__(self):
        self.snake_body = [] #a buffer to hold all turtle objects
        self.build_baby_snake()
        self.snake_p1 = self.snake_body[0]
    
        
    def build_baby_snake(self):
        """creates the initial snake objects"""
        for position in snake_position:
            self.construct_snake(position)  
              
    def construct_snake(self, position):
        """creates seperate turtle objects"""
        snake = turtle.Turtle()
        snake.penup()
        snake.color('white')
        snake.shape('square')
        snake.setposition(position, 0)
        self.snake_body.append(snake)
            
    def grow(self):
        """adds a newly constructed snake to self.snake_body"""
        self.construct_snake(self.snake_body[-1].xcor())

    def give_motion(self):
        """holds all turtle objects together"""
        for i in range(len(self.snake_body)-1, 0, -1):
            self.snake_body[i].setposition(self.snake_body[i-1].position())
        return self.snake_p1.fd(20)
    
    #internal controls of turtle
    def control_up(self):
        if self.snake_p1.heading() != 270: 
            self.snake_p1.setheading(90)

    def control_down(self):
        if self.snake_p1.heading() != 90:
            self.snake_p1.setheading(270)

    def control_left(self):
        if self.snake_p1.heading() != 0:
            self.snake_p1.setheading(180)

    def control_right(self):
        if self.snake_p1.heading() != 180:
            self.snake_p1.setheading(0)

