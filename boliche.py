
class Boliche:
    plays_game = [0 for i in range(20)]
    actual_played = 0

    def play_score(self):
        [sum_value, index]=[0,0]

        #frame 0-9 com passo igual à 2.
        #for i in range(0,20,2):
        for i in range(0, 10):
            sum_value+=self.plays_game[index]+self.plays_game[(index+1)]
            index+=2
            #sum_value = self.plays_game[i+1]+self.plays_game[i]
        return sum_value
        #return sum(self.plays_game)


    def play(self,value):
        self.plays_game[self.actual_played] = value
        self.actual_played+=1
