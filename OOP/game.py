class Game:
    def __init__(self, name, score=0):
        self.name = name
        self.score = score

    def start(self):
        print(f"Starting game {self.name}")
        self.score = 0
    
    def end(self):
        print(f"Ending game {self.name}")
    
    def add_score(self, points):
        self.score += points
        print(f"Added {points} points to {self.name}")

class ActionGame(Game):
    def __init__(self, name, lives=3):
        super().__init__(name)
        self.lives = lives
    
    def die(self):
        self.lives -= 1
        if self.lives == 0:
            self.end()
        else:
            print(f"{self.name} lost a life")

game = ActionGame("Super Mario Bros.")
game.start()
game.add_score(100)
game.die()
game.die()
game.die()
