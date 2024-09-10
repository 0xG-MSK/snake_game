#class, modules from sister files
import turtle 
import time
import snake
import food
import score

turtle.speed(0)

#inputs
try:
    #sets the game setup
    x = turtle.numinput(title="Game Setup Width", prompt="Choose the width of the game: \n width: 660 * height: 325 - recommended")
    y = turtle.numinput(title="Game Setup Height", prompt="Enter the height of the game: \n width: 660 * height: 325 - recommended")
    if x > 10000:
       x = 600
    if y > 10000:
       y = 600
except:
    x = 600
    y = 600
    

#objects from classes
snake = snake.Snake()
score = score.Score(x, y)
food = food.Food(x, y)

CUSTOM_BACKIMG = "21224312416.gif"
   

#constants for user's screen dimension
SCREEN_HEIGHT_neg = -score.y
SCREEN_HEIGHT_pos = abs(SCREEN_HEIGHT_neg)

SCREEN_WIDTH_neg = -score.x
SCREEN_WIDTH_pos = abs(SCREEN_WIDTH_neg)

#creates a screen object
screen = turtle.Screen()

screen.setup(x, y) #set the game window dimensions

#trys to set screen backgroung to the img of choice
try:
    screen.bgpic(CUSTOM_BACKIMG)
except:
    screen.bgcolor("black")
#sets the tracer time to faster, to avoid animations to joined turtles
screen.tracer(0)


#listens to inputs
screen.listen()

#CONTROLS FOR SNAKE

screen.onkey(snake.control_down, 's')
screen.onkey(snake.control_down, 'Down')

screen.onkey(snake.control_up, 'w')
screen.onkey(snake.control_up, 'Up')
    
screen.onkey(snake.control_left, 'a')
screen.onkey(snake.control_left, 'Left')
    
screen.onkey(snake.control_right, 'd')
screen.onkey(snake.control_right, 'Right')

#starts the game
game_on = True
while game_on:
    turtle.update() #updates the screen
    time.sleep(score.PACE_SPEED)#sets updates timer, snake movement speed
    #from snake.py file| starts the snake's movemoent
    snake.give_motion()
        
    score.show_score()#from score.py| shows the number of hits with food object
    
    
    if snake.snake_p1.distance(food) < 20 :
        """Detects interaction with food turtle object"""
        food.food_placement()#from food.py| sets random food turtle location
        snake.grow()#from snake.py| grows snake
        score.update_score()#from score.py| updates the score
        
    if snake.snake_p1.xcor() > SCREEN_WIDTH_pos or snake.snake_p1.xcor() < SCREEN_WIDTH_neg or snake.snake_p1.ycor() > SCREEN_HEIGHT_pos or snake.snake_p1.ycor() < SCREEN_HEIGHT_neg:
        #checks whether snake collide with screen dimentions given(walls)
        game_on = False
        score.game_over()#from score.py| shows when game over
        
    for part in snake.snake_body[1:]:
        #detects collision with its other turtle objects
        if snake.snake_p1.distance(part) < 10:
            game_on = False
            score.game_over()
            score.humor_death()
     
    score.pro_player() #enhaces difficulty

screen.exitonclick()      