from requests.status_codes import codes

LIKES = "likes"


def test_get_likes_success(likes_response):
    """
    Test the status code of the response for getting likes.

    :param likes_response: The response object.
    :return: None
    :raises AssertionError: If the response status code is not equal to `status_codes.ok`.
    """
    assert likes_response.status_code == codes.ok


def test_get_likes_max(likes_response_data):
    """
    Test whether the number of likes retrieved is within the expected maximum limit.

    :param likes_response_data: The data representing the number of likes retrieved.
    :return: None
    :raises AssertionError: If the number of likes is greater than 9999.
    """
    assert likes_response_data.get(LIKES) <= 9999


def test_get_likes_min(likes_response_data):
    """
    Test whether the number of likes retrieved is above the expected minimum limit.

    :param likes_response_data: The data representing the number of likes retrieved.
    :return: None
    :raises AssertionError: If the number of likes is less than 1000.
    """
    assert likes_response_data.get(LIKES) >= 1000


def test_get_likes_type(likes_response_data):
    """
    Test whether the data type of the number of likes is as expected.

    :param likes_response_data: The data representing the number of likes retrieved.
    :return: None
    :raises AssertionError: If the data type of the number of likes is not `int`.
    """
    assert type(likes_response_data.get(LIKES)) == int
