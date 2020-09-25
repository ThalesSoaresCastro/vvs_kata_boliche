import pytest
from boliche import Boliche

play_boliche = lambda b,x,arr_size: [b.play(x) for i in range(arr_size)]

class TestBoliche:

    def test_score_all_0(self):
        b=Boliche()
        result = 0
        input_score = play_boliche(b,0, 20)
        score = b.play_score()
        assert result == score
        
    def test_score_all_1(self):
        b=Boliche()
        result = 20
        input_score = play_boliche(b,1,20)
        score = b.play_score()
        assert result == score
        
    # def test_spare_score_16(self):
    #     result = 16
    #     input_score = list_input()
    #     score = boliche_game(input_score)
    #     assert result == score
    
