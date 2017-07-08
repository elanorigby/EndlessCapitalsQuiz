from ccquiz.logic import Quiz
import pytest

@pytest.fixture(params=['capitals', 'countries', 'random'])
def kind(request):
    return Quiz(request.param)

def test_ans_gets_true(kind):
    """" assert the answer == the answer """
    assert kind.is_correct(kind.ans) == True


def test_wrong_gets_false(kind):
    """" assert somebullshit != the answer """
    assert kind.is_correct('Townsville') == False


def test_hint_gets_false(kind):
    """" assert the hint != the answer """
    if kind == 'Monaco':
        pass
    else:
        assert kind.is_correct(kind.hint) == False

