import pytest
import requests
import urllib.parse

BASE_URL = "http://127.0.0.1:8000"
POSTS = "posts"
LIKES = "likes"
FOLLOWERS = "followers"


@pytest.fixture(scope="session")
def posts_response():
    post_url = urllib.parse.urljoin(BASE_URL, POSTS)
    return requests.get(post_url)


@pytest.fixture()
def posts_response_data(posts_response):
    return posts_response.json().get(POSTS)


@pytest.fixture()
def likes_response():
    likes_url = urllib.parse.urljoin(BASE_URL, LIKES)
    return requests.get(likes_url)


@pytest.fixture()
def likes_response_data(likes_response):
    return likes_response.json().get(LIKES)


@pytest.fixture()
def followers_response():
    followers_url = urllib.parse.urljoin(BASE_URL, FOLLOWERS)
    return requests.get(followers_url)


@pytest.fixture()
def followers_response_data(followers_response):
    return followers_response.json().get(FOLLOWERS)
