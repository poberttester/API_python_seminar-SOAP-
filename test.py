from SOAP_API import check_text
import pytest


def test_func(good_word, bad_word):
    assert good_word in check_text(bad_word)


if __name__ == '__main__':
    pytest.main(['-v'])