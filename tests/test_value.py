from micrograd.engine import Value


def test_value_add():
    assert Value(2.0) + Value(3.0) == Value(5.0)
