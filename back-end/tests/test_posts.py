def test_get_posts_success(posts_response):
    assert posts_response.status_code == 200


def test_get_posts_max(posts_response):
    assert posts_response.json().get("posts") <= 99


def test_get_posts_min(posts_response):
    assert posts_response.json().get("posts") >= 0


def test_get_posts_type(posts_response):
    assert type(posts_response.json().get("posts")) == int
