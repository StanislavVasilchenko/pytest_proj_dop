import pytest

from utils.dict import get_val

dict_ = {"vcs": "mercurial"}


@pytest.mark.parametrize("collection, key, default, result", [(dict_, "vcs", "git", "mercurial"),
                                                              ({}, "vcs", "git", "git"),
                                                              ({}, "vcs", "bazaar", "bazaar"),
                                                              (dict_, "asd", "git", "git")])
def test_get_val(collection, key, default, result):
    assert get_val(collection, key, default) == result


@pytest.mark.parametrize("error, coll, key", [(TypeError, ["dict_"], "sdf")])
def test_get_val_error(error, coll, key):
    with pytest.raises(error):
        get_val(coll, key)
