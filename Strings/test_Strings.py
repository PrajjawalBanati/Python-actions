import Strings
def test_show():
    recieved=Strings.show()
    assert recieved=="hello world"
def test_make():
    mask=Strings.make()
    assert mask=="self"
