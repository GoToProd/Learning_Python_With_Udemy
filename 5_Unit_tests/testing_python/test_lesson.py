import pytest

# @pytest.mark.one
# def test_equal():
#     assert 1 == 1, 'Good'


# @pytest.mark.two
# def test_notEqual():
#     assert 1 != 2, 'Bad'


# def test_square():
#     n = 2
#     assert n*n == 4


def getReply(number):
    if number % 3 == 0 and number % 5 == 0:
        return 'FizzBuzz'
    elif number % 3 == 0:
        return 'Fizz'
    elif number % 5 == 0:
        return 'Buzz'
    return ''


def test_fizz():
    number = 3
    assert getReply(number) == 'Fizz'


def test_buzz():
    number = 5
    assert getReply(number) == 'Buzz'


def test_FizzBuzz():
    number = 15
    assert getReply(number) == 'FizzBuzz'
