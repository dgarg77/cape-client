import pytest
from .fixtures import cc


def test_answer(cc):
    token = cc.get_user_token()
    answers = cc.answer(token, "Is this API easy to use?")
    assert len(answers) == 1
    assert answers[0]["text"] is not None


def test_multiple_answers(cc):
    token = cc.get_user_token()
    answers = cc.answer(token, "Is this API easy to use?", number_of_items=2)
    assert len(answers) == 2


def test_document_ids(cc):
    token = cc.get_user_token()
    answers = cc.answer(token, "Is this API easy to use?", document_ids=["358e1b77c9bcc353946dfe107d6b32ff"])
    assert len(answers) == 1