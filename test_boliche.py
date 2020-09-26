import pytest
from boliche import Boliche


play_boliche = lambda b,x,arr_size: [b.play(x) for i in range(arr_size)]
  
play_array_boliche = lambda b,arr: [b.play(arr[i]) for i in range(len(arr))] 

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
        play_array_boliche(boliche,[5,5,3])
        score = boliche.play_score()
        assert result == score
    
    def test_strike_score_24(self, boliche):
        result = 24
        """
            Teste de Strike:
            -Primeira chamada do método play() com valor 10;
            -Segunda chamada do método play() com valor 3;
            -Terceira chamada do método play() com valor 4;

        """
        play_array_boliche(boliche,[10, 3, 4])
        play_boliche(boliche,0,16)
        score = boliche.play_score()

        assert result == score

    def test_perfect_score_300(self, boliche):
        result = 300

        play_boliche(boliche,10, 12)

        score = boliche.play_score()
        assert result == score