
class Boliche:
    #plays_game = [0 for i in range(21)]
    #actual_played = 0
    def __init__(self):
        self.plays_game = [0 for i in range(21)]
        self.actual_played = 0

    def play_score(self):
        [sum_value, index]=[0,0]

        for i in range(0, 10):
            if (self.plays_game[index]+self.plays_game[(index+1)]) == 10:
                sum_value+= 10 + self.plays_game[i+2]
                index+=2
            else:
                sum_value+=self.plays_game[index]+self.plays_game[(index+1)]
                index+=2
        return sum_value


    def play(self,value):
        self.plays_game[self.actual_played] = value
        self.actual_played+=1


# b=Boliche()

# b.play(5)
# b.play(5)
# b.play(3)
# print(b.play_score())