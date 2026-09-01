from app import app


def client():
    app.config.update(TESTING=True)
    return app.test_client()


def test_lists_all_widgets():
    resp = client().get("/widgets")
    assert resp.status_code == 200
    assert len(resp.get_json()) == 5


def test_limit_caps_results():
    resp = client().get("/widgets?limit=2")
    assert [w["id"] for w in resp.get_json()] == [1, 2]
