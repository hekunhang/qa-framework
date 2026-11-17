import pytest

@pytest.fixture(scope="session")
def token():
    """整个测试会话只登录一次，返回 token"""
    print("\n>>> 执行登录（只应该看到一次）")
    return "fake-token-123456"

@pytest.fixture
def auth_headers(token):
    """用例需要时自动带上鉴权头，token 来自上面的 token fixture"""
    return {"Authorization": f"Bearer {token}"}
