from requests import status_codes


def test_get_followers_success(followers_response):
    assert followers_response.status_code == status_codes.ok


def test_get_followers_max(followers_response_data):
    assert followers_response_data <= 999


def test_get_followers_min(followers_response_data):
    assert followers_response_data >= 100


def test_get_followers_type(followers_response_data):
    assert type(followers_response_data) == int
