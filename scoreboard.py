from turtle import  Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.highscore = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()


    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score} High score: {self.highscore}' , align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
        
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over!", align=ALIGNMENT, font=FONT)

    def reset_scoreboard(self):

        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()