from pathlib import Path
import yaml
import pytest

from api.httpbin_api import HttpbinApi

api = HttpbinApi()

DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "get_cases.yaml"
with open(DATA_FILE, "r", encoding="utf-8") as f:
    CASES = yaml.safe_load(f)


@pytest.mark.parametrize("case", CASES, ids=[c["title"] for c in CASES])
def test_get_with_params(case):
    resp = api.get_with_params(case["params"])
    assert resp.status_code == 200
    # 逐个校验每个参数都被原样回传
    for key, value in case["params"].items():
        assert resp.json()["args"][key] == value
