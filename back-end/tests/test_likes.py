def test_get_likes_success(likes_response):
    assert likes_response.status_code == 200


def test_get_likes_max(likes_response_data):
    assert likes_response_data <= 9999


def test_get_likes_min(likes_response_data):
    assert likes_response_data >= 1000


def test_get_likes_type(likes_response_data):
    assert type(likes_response_data) == int
