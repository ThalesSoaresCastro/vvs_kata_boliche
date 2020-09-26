
class Boliche:
    #plays_game = [0 for i in range(21)]
    #actual_played = 0
    def __init__(self):
        self.plays_game = [0 for i in range(21)]
        self.actual_played = 0

    def play_score(self):
        [sum_value, index]=[0,0]

        for i in range(0, 10):

            if self.strike_verify(index):
                sum_value += 10 + self.strike_frame_sum(index)
                index+=1

            elif self.spare_verify(index) :
                sum_value+= 10 + self.spare_frame_sum(index)
                index+=2

            else:
                sum_value += self.ball_frame_sum(index)
                index+=2

        return sum_value

    def ball_frame_sum(self, index):
        return self.plays_game[index]+self.plays_game[(index+1)]

    def strike_frame_sum(self, index):
        return self.plays_game[index+1] + self.plays_game[index+2] 

    def spare_frame_sum(self, index):
        return self.plays_game[index+2]
      
    def spare_verify(self,frame):
        return (self.plays_game[frame]+self.plays_game[(frame+1)]) == 10

    def strike_verify(self, frame):
        return self.plays_game[frame] == 10

    def play(self,value):
        self.plays_game[self.actual_played] = value
        self.actual_played+=1


# b=Boliche()

# b.play(5)
# b.play(5)
# b.play(3)
# print(b.play_score())