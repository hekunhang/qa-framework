import requests

def test_get_hello():
    url = "https://httpbin.org/get"
    resp = requests.get(url)
    # 断言响应状态码等于200
    assert resp.status_code == 200
    print("响应结果：", resp.json())
