import pytest 
from src.E_2_3_5 import *

def test_contraseña5_1():
    with pytest.raises(ValueError):
        contraseña5("a")


@pytest.mark.parametrize(
    "input_x,expected",
    [
        ("contraseña_segura","La contraseña correcta es: contraseña_segura")
    ]
)

def test_contraseña5(input_x,expected):
    assert contraseña5(input_x) == expected