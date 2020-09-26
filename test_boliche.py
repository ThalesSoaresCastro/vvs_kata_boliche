import pytest
from boliche import Boliche


play_boliche = lambda b,x,arr_size: [b.play(x) for i in range(arr_size)]

class TestBoliche:

    @pytest.fixture(scope='function')
    def boliche(self):
        return Boliche()

    def test_score_all_0(self, boliche):
        result = 0
        play_boliche(boliche,0, 20)
        score = boliche.play_score()
        assert result == score
    
    def test_score_all_1(self, boliche):
        result = 20
        play_boliche(boliche,1,20)
        score = boliche.play_score()
        assert result == score

    def test_spare_score_16(self, boliche):
        result = 16
        boliche.play(5)
        boliche.play(5)
        boliche.play(3)
        score = boliche.play_score()
        assert result == score
    
