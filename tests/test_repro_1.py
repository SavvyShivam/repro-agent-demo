def test_limit_zero_returns_empty():
    from app import app
    app.config.update(TESTING=True)
    resp = app.test_client().get("/widgets?limit=0")
    assert resp.status_code == 200
    assert resp.get_json() == []
