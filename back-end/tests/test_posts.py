from requests import status_codes


def test_get_posts_success(posts_response):
    """
    Test the status code of the response for getting posts.

    :param posts_response: The response object.
    :return: None
    :raises AssertionError: If the response status code is not equal to `status_codes.ok`.
    """
    assert posts_response.status_code == status_codes.ok


def test_get_posts_max(posts_response_data):
    """
    Test whether the number of posts retrieved is within the expected maximum limit.

    :param posts_response_data: The data representing the number of posts retrieved.
    :return: None
    :raises AssertionError: If the number of posts is greater than 99.
    """
    assert posts_response_data <= 99


def test_get_posts_min(posts_response_data):
    """
    Test whether the number of posts retrieved is above the expected minimum limit.

    :param posts_response_data: The data representing the number of posts retrieved.
    :return: None
    :raises AssertionError: If the number of posts is less than 0.
    """
    assert posts_response_data >= 0


def test_get_posts_type(posts_response_data):
    """
    Test whether the data type of the number of posts is as expected.

    :param posts_response_data: The data representing the number of posts retrieved.
    :return: None
    :raises AssertionError: If the data type of the number of posts is not `int`.
    """
    assert type(posts_response_data) == int
