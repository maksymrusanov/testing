import pytest
import time
import source.my_fucntions as my_functions


def test_add():
    result = my_functions.add(1, 4)
    assert result == 5


def test_add_strings():
    result = my_functions.add("i like ", "burgers")
    assert result == "i like burgers"


def test_divide():
    result = my_functions.divide(4, 2)
    assert result == 2


def test_divide_by_zero():
    with pytest.raises(ValueError):
        my_functions.divide(10, 0)


@pytest.mark.slow
def test_slow():
    time.sleep(5)
    result = my_functions.divide(4, 2)
    assert result == 2


@pytest.mark.skip(reason="this feature is curr broken")
def test_add():
    assert my_functions.add(1, 2) == 3


@pytest.mark.xfail(reason="can`t divide by zero")
def test_divide_zero():
    my_functions.divide(10, 0)
