# import pytest
from boliche import boliche_game

list_input = lambda x,arr_size: [x for i in range(arr_size)]

class TestBoliche:

    def test_score_all_0(self):
        result = 0
        input_score = list_input(0, 20)
        score = boliche_game(input_score)
        assert result == score
    
    def test_score_all_1(self):
        result = 20
        input_score = list_input(1,20)
        score = boliche_game(input_score)
        assert result == score
    
