from requests import status_codes


def test_get_followers_success(followers_response):
    """
    Test the status code of the response.

    :param followers_response: The response object.
    :return: None
    :raises AssertionError: If the response status code is not equal to `status_codes.ok`.
    """
    assert followers_response.status_code == status_codes.ok


def test_get_followers_max(followers_response_data):
    """
    Test whether the number of followers retrieved is within the expected maximum limit.

    :param followers_response_data: The data representing the number of followers retrieved.
    :return: None
    :raises AssertionError: If the number of followers is greater than 999.
    """
    assert followers_response_data <= 999


def test_get_followers_min(followers_response_data):
    """
    Test whether the number of followers retrieved is above the expected minimum limit.

    :param followers_response_data: The data representing the number of followers retrieved.
    :return: None
    :raises AssertionError: If the number of followers is less than 100.
    """
    assert followers_response_data >= 100


def test_get_followers_type(followers_response_data):
    """
    Test whether the data type of the number of followers is as expected.

    :param followers_response_data: The data representing the number of followers retrieved.
    :return: None
    :raises AssertionError: If the data type of the number of followers is not `int`.
    """
    assert type(followers_response_data) == int
