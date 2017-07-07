from ccquiz.logic import Quiz
import pytest

# capitals ---------
# instantiate
@pytest.fixture
def caps():
    return Quiz('capitals')

# assert quiz.ans -> true
def test_ans_gets_true(caps):
    """" pass answer as guess."""
    assert caps.is_correct(caps.ans) == True

# assert somebullshit -> false
def test_wrong_gets_false(caps):
    """" pass random bs as guess"""
    assert caps.is_correct('Townsville') == False

def test_country_gets_false(caps):
    """" pass hint as guess"""
    assert caps.is_correct(caps.hint) == False


