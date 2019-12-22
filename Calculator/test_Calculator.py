import Calculator
def test_add():
    total=Calculator.add(4,5)
    assert total==9
def test_subtract():
    total=Calculator.subtract(9,5)
    assert total==4
def test_multiply():
    total=Calculator.multiply(10,3)
    assert total==30
def test_divide():
    total=Calculator.divide(9,3)
    assert total==3
