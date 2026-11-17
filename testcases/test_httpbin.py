from api.httpbin_api import HttpbinApi

api = HttpbinApi()

def test_get_demo():
    resp = api.get_demo(who="autotest")
    assert resp.status_code == 200
    assert resp.json()["args"]["who"] == "autotest"


def test_post_demo():
    resp = api.post_demo(name="hekunhang", job="自动化测试")
    assert resp.status_code == 200
    assert resp.json()["json"]["name"] == "hekunhang"


def test_status_404():
    resp = api.get_status(404)
    assert resp.status_code == 404
