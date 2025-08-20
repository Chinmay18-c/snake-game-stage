from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 270)
        stage = self.get_stage()
        self.write(f"Score: {self.score}   High Score: {self.high_score}   Stage: {stage}",
                   align="center", font=('Courier', 16, 'normal'))

    def get_stage(self):
        if self.score < 10:
            return 1
        elif self.score < 25:
            return 2
        else:
            return 3

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!\nPress 'R' to Restart", align="center", font=('Courier', 20, 'bold'))

    def start_message(self):
        self.goto(0, 0)
        self.write("Press SPACE to Start", align="center", font=('Courier', 20, 'bold'))

    def increase_scoreboard(self):
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as file:
                file.write(str(self.high_score))
        self.update_scoreboard()

    def reset_score(self):
        self.score = 0
