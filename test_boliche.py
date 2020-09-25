import pytest
from boliche import Boliche


play_boliche = lambda b,x,arr_size: [b.play(x) for i in range(arr_size)]

class TestBoliche:

    @pytest.fixture(autouse=True)
    def boliche(self):
        return Boliche()

    def test_score_all_0(self, boliche):
        result = 0
        input_score = play_boliche(boliche,0, 20)
        score = boliche.play_score()
        assert result == score
        
    def test_score_all_1(self, boliche):
        result = 20
        input_score = play_boliche(boliche,1,20)
        score = boliche.play_score()
        assert result == score
        
    # def test_spare_score_16(self):
    #     result = 16
    #     input_score = list_input()
    #     score = boliche.play_score()
    #     assert result == score
    
