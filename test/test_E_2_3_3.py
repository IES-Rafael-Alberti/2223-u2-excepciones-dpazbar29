import pytest 
from src.E_2_3_3 import *

def test_cuentaAtras():
    with pytest.raises(ValueError):
        cuentaAtras(-2)


@pytest.mark.parametrize(
        "input_x,expected",
        [
            (8,"8,7,6,5,4,3,2,1")
        ]
)
def test_cuentaAtras1(input_x,expected):
    assert cuentaAtras(input_x) == expected


@pytest.mark.parametrize(
    "input_x,expected",
    [
        ("1,3,5,7","Resultado: 1,3,5,7")
    ]
)

def test_mensajeSalida3(input_x,expected):
    assert mensajeSalida3(input_x) == expected