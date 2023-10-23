import pytest 
from src.E_2_3_4 import *

def test_mensajeSalida4_1():
    with pytest.raises(ValueError):
        mensajeSalida4("a")


@pytest.mark.parametrize(
    "input_x,expected",
    [
        (3,"El número ingresado es: 3")
    ]
)

def test_mensajeSalida4(input_x,expected):
    assert mensajeSalida4(input_x) == expected
