from bank import value

def test_value_1():
    assert value("Hello") == 0
    assert value("Hello ") == 0

def test_value_2():
    assert value("Hello, Newman") == 0
    assert value("How you doing?") == 20
    
def test_value_3():
    assert value("What's happening?") == 100
    assert value("What's up?") == 100
