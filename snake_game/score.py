from turtle import Turtle


class Score(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.setposition(0, 325)
        self.color('white')
        self.score = 0
        self.PACE_SPEED = 0.1
        self.x = x
        self.y = y
        
    def show_score(self):
        """shows the score of the game"""
        self.setposition(0, self.y)
        self.write(arg= f'SCORE: {self.score}', align="center")
        
    def humor_death(self):
        """a death announcement with humor"""
        self.setposition(0, -55)
        self.clear()
        self.color("slate blue")
        self.write(arg= f'SCORE: {self.score}', align="center")
        self.write("You basically ate yourself :\ . Try eating the apple rather than your body", align="center")
        
    def game_over(self):
        """declares game over"""
        self.clear()
        self.home()
        self.color('red')
        self.write("GAME OVER", align="center")
        self.goto(0, -30)
        self.color("blue")
        self.write(f"SCORE: {self.score}", align="center")
        
    def update_score(self):
        """updates the score everytime"""
        self.score += 1
        self.clear()
        self.show_score()
        
    def pro_player(self):
       """enhances attribures for more difficulty"""
       if self.score == 15:
           self.clear()
           self.home()
           self.color("cornflower blue")
           self.write("You are a mini-pro here, you now have to lock IN!", align="center")
           self.PACE_SPEED = 0.065
           
       if self.score == 25:
           self.clear()
           self.home()
           self.color("orange red")
           self.write('Oh i see you are a pro, bring your best', align="center")
           self.PACE_SPEED = 0.055
           
       if self.score == 35:
           self.clear()
           self.home()
           self.color("indigo")
           self.write('There is no way you are still here. HAHAHA, bring all you got', align="center")
           self.PACE_SPEED = 0.035
           
       if self.score == 45:
           self.clear()
           self.home()
           self.color("dark violet")
           self.write("This will now be the end of you", align="center")
           self.PACE_SPEED = 0.025
           
       
    