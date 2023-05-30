import pytest
import requests
import urllib.parse
from requests import Response

BASE_URL = "http://127.0.0.1:8000"


@pytest.fixture(scope="session")
def posts_response() -> Response:
    """
    Get the response for the posts API.

    :return: The response object from the API request.
    """
    post_url = urllib.parse.urljoin(BASE_URL, "posts")
    return requests.get(post_url)


@pytest.fixture()
def posts_response_data(posts_response) -> dict:
    """
    Get the data for the posts from the posts response.

    :param posts_response: The response object from the posts API.
    :return: A dictionary containing the data for the posts.
    """
    return posts_response.json()


@pytest.fixture()
def likes_response() -> Response:
    """
    Get the response for the likes API.

    :return: The response object from the API request.
    """
    likes_url = urllib.parse.urljoin(BASE_URL, "likes")
    return requests.get(likes_url)


@pytest.fixture()
def likes_response_data(likes_response) -> dict:
    """
    Get the data for the likes from the likes response.

    :param likes_response: The response object from the likes API.
    :return: A dictionary containing the data for the likes.
    """
    return likes_response.json()


@pytest.fixture()
def followers_response() -> Response:
    """
    Get the response for the followers API.

    :return: The response object from the API request.
    """
    followers_url = urllib.parse.urljoin(BASE_URL, "followers")
    return requests.get(followers_url)


@pytest.fixture()
def followers_response_data(followers_response) -> dict:
    """
    Get the data for the followers from the followers response.

    :param followers_response: The response object from the followers API.
    :return: A dictionary containing the data for the followers.
    """
    return followers_response.json()


@pytest.fixture()
def data_response() -> Response:
    """
    Get the response for the data API.

    :return: The response object from the API request.
    """
    data_url = urllib.parse.urljoin(BASE_URL, "data")
    return requests.get(data_url)


@pytest.fixture()
def data_response_json(data_response) -> dict:
    """
    Get the JSON data from the data response.

    :param data_response: The response object from the data API.
    :return: A dictionary containing the JSON data.
    """
    return data_response.json()
