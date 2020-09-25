# import pytest
from boliche import boliche_game

class TestBoliche:
    def test_score0(self):
        result = 0
        input_score = list(0 for i in range(20))
        score = boliche_game(input_score)
        assert result == score
    
    def test_score_all_1(self):
        result = 20
        input_score = list(1 for i in range(20))
        score = boliche_game(input_score)
        assert result == score
        