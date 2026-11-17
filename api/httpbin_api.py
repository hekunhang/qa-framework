from common.request_util import req

class HttpbinApi:
    """httpbin 接口集合：一个方法对应一个接口"""

    def get_demo(self, who=None):
        params = {"who": who} if who else None
        return req.get("/get", params=params)

    def post_demo(self, name, job):
        return req.post("/post", json={"name": name, "job": job})

    def get_status(self, code):
        return req.get(f"/status/{code}")

    def get_bearer(self, headers=None):
        return req.get("/bearer", headers=headers)

    def get_with_params(self, params=None):
        return req.get("/get", params=params)
