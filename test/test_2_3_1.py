import pytest 
from src.E_2_3_1 import *



def test_secuenciaAños1():
    with pytest.raises(ValueError):
        secuenciaAños(-2)


@pytest.mark.parametrize(
        "input_x,expected",
        [
            (3,"1,2,3")
        ]
)
def test_secuenciaAños(input_x,expected):
    assert secuenciaAños(input_x) == expected


@pytest.mark.parametrize(
    "input_x,expected",
    [
        ("1,2,3","Años cumplidos 1,2,3")
    ]
)

def test_mensajeSalida1(input_x,expected):
    assert mensajeSalida1(input_x) == expected