import pytest

from utils.dict import get_val

dict_ = {"vcs": "mercurial"}


@pytest.mark.parametrize("collection, key, default, result", [(dict_, "vcs", "git", "mercurial"),
                                                              ({}, "vcs", "git", "git"),
                                                              ({}, "vcs", "bazaar", "bazaar"),
                                                              (dict_, "asd", "git", "git")])
def test_get_val(collection, key, default, result):
    assert get_val(collection, key, default) == result

