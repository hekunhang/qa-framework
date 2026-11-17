from api.httpbin_api import HttpbinApi

api = HttpbinApi()

def test_bearer_with_token(auth_headers):
    resp = api.get_bearer(auth_headers)
    assert resp.status_code == 200
    assert resp.json()["authenticated"] is True

def test_bearer_without_token():
    resp = api.get_bearer()
    assert resp.status_code == 401
