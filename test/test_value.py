import pytest
from micrograd.engine import Value

def test_value_forward_pass():
    a = Value(2.0)
    b = Value(3.0)
    c = a + b
    assert c.data == 5.0
