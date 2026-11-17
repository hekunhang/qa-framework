import requests
from common.config_loader import BASE_URL, TIMEOUT
from common.logger import logger

class RequestUtil:
    def __init__(self, base_url=BASE_URL, timeout=TIMEOUT):
        self.base_url = base_url
        self.timeout = timeout
        self.session = requests.Session()

    def get(self, path, params=None, headers=None):
        url = self.base_url + path
        logger.info(f"GET  {url}  params={params}")
        resp = self.session.get(url, params=params, headers=headers, timeout=self.timeout)
        logger.info(f"  -> {resp.status_code}  {resp.text[:300]}")
        return resp

    def post(self, path, data=None, json=None, headers=None):
        url = self.base_url + path
        logger.info(f"POST {url}  json={json}")
        resp = self.session.post(url, data=data, json=json, headers=headers, timeout=self.timeout)
        logger.info(f"  -> {resp.status_code}  {resp.text[:300]}")
        return resp

req = RequestUtil()
