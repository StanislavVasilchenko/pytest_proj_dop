import pytest

from utils.dict import get_val


@pytest.fixture
def collection():
    return {"vcs": "mercurial"}


def test_get_val(collection):
    assert get_val(collection, "vcs") == "mercurial"
    assert get_val(collection, "vcs", "git") == "mercurial"
    assert get_val({}, "vcs", "git") == "git"
    assert get_val({}, "vcs", "bazaar") == "bazaar"
