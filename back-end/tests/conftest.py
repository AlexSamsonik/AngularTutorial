import pytest
import requests


@pytest.fixture()
def posts_response():
    return requests.get("http://127.0.0.1:8000/posts")
