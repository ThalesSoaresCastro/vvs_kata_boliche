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
        """
            Rolando o spare:
                chama play() com valor 5 duas vezes seguidas
                e em seguida chama o play() mais uma vez mas com valor 3. 
        """
        play_boliche(boliche,5,2)
        boliche.play(3)
        score = boliche.play_score()
        assert result == score
    
    def test_strike_score_24(self, boliche):
        result = 24
        
        boliche.play(10)
        boliche.play(3)
        boliche.play(4)
        play_boliche(boliche,0,16)
        score = boliche.play_score()

        assert result == score

