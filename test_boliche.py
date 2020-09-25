# import pytest
from boliche import boliche_game

class TestBoliche:
    def test_score0(self):
        result = 0
        input_score = list(0 for i in range(20))
        score = boliche_game(input_score)
        assert result == score