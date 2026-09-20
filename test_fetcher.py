from fetcher import get_user, build_report

def test_real_user():
    data = get_user("torvalds")
    assert data is not None

def test_missing_user():
    data = get_user("this-user-does-not-exist-999")
    assert data is None

def test_report_format():
    report = build_report("torvalds")
    assert "repos" in report