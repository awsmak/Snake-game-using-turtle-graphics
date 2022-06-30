from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.write(arg=f'Score : {self.score}', move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f'Score : {self.score}', move=False, align='center', font=('Arial', 24, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write(arg='GAME OVER', move=False, align='center', font=('Arial', 24, 'normal'))
