from bsync import bsync


def test_initialize():
    b = bsync.BuildingSync()
    assert b is not None


def test_int_datatype():
    b = bsync.Sections.Section.Story(1)
    assert b is not None
