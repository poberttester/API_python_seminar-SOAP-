import pytest


@pytest.fixture()
def good_word():
    return "ошибка"


@pytest.fixture()
def bad_word():
    return "ашибка"
