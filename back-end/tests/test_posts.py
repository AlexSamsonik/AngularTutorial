def test_get_posts_success(posts_response):
    assert posts_response.status_code == 200


def test_get_posts_max(posts_response_data):
    assert posts_response_data <= 99


def test_get_posts_min(posts_response_data):
    assert posts_response_data >= 0


def test_get_posts_type(posts_response_data):
    assert type(posts_response_data) == int
