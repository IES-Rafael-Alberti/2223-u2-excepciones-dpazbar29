import pytest 
from src.E_2_3_2 import *

def test_numerosImpares():
    with pytest.raises(ValueError):
        numerosImpares(-2)


@pytest.mark.parametrize(
        "input_x,expected",
        [
            (8,"1,3,5,7")
        ]
)
def test_numerosImapres1(input_x,expected):
    assert numerosImpares(input_x) == expected


@pytest.mark.parametrize(
    "input_x,expected",
    [
        ("1,3,5,7","Numeros impares 1,3,5,7")
    ]
)

def test_mensajeSalida2(input_x,expected):
    assert mensajeSalida2(input_x) == expected