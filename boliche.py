
class Boliche:
    plays_game = [0 for i in range(20)]
    actual_played = 0

    def play_score(self):
        return sum(self.plays_game)


    def play(self,value):
        self.plays_game[self.actual_played] = value
        self.actual_played+=1
