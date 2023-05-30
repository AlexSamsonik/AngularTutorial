from requests.status_codes import codes

MESSAGE = "message"


def test_response_status_code(data_response):
    """
    Test the status code of the response.

    :param data_response: The response object.
    :return: None
    :raises AssertionError: If the response status code is not equal to `status_codes.ok`.
    """
    assert data_response.status_code == codes.ok


def test_successful_response(data_response_json):
    """
    Test that the response contains a successful message.

    :param data_response_json: The JSON response data.
    :return: None
    :raises AssertionError: If the "message" key in the response does not have the expected value.
    """
    assert data_response_json.get(MESSAGE) == "Hello FastAPI"


def test_response_data_type(data_response_json):
    """
    Test the data type of the response.

    :param data_response_json: The JSON response data.
    :return: None
    :raises AssertionError: If the response data is not of type dict.
    """
    assert isinstance(data_response_json, dict)


def test_message_key_exists(data_response_json):
    """
    Test that the "message" key exists in the response.

    :param data_response_json: The JSON response data.
    :return: None
    :raises AssertionError: If the "message" key does not exist in the response.
    """
    assert MESSAGE in data_response_json


def test_message_value(data_response_json):
    """
    Test the value of the "message" key in the response.

    :param data_response_json: The JSON response data.
    :return: None
    :raises AssertionError: If the value of the "message" key is not equal to "Hello FastAPI".
    """
    assert data_response_json.get(MESSAGE) == "Hello FastAPI"


def test_message_value_type(data_response_json):
    """
    Test the data type of the value of the "message" key in the response.

    :param data_response_json: The JSON response data.
    :return: None
    :raises AssertionError: If the value of the "message" key is not of type str.
    """
    assert isinstance(data_response_json.get(MESSAGE), str)


def test_response_structure(data_response_json):
    """
    Test the structure of the response.

    :param data_response_json: The JSON response data.
    :return: None
    :raises AssertionError: If the response contains keys other than "message".
    """
    assert set(data_response_json.keys()) == {MESSAGE}


def test_response_content_type(data_response):
    """
    Test the content type of the response.

    :param data_response: The response object.
    :return: None
    :raises AssertionError: If the "Content-Type" header in the response is not equal to "application/json".
    """
    assert data_response.headers.get("Content-Type") == "application/json"


def test_response_server_name(data_response):
    """
    Test the server name in the response headers.

    :param data_response: The response object.
    :return: None
    :raises AssertionError: If the "server" header in the response is not equal to "uvicorn".
    """
    assert data_response.headers.get("server") == "uvicorn"


def test_response_time(data_response):
    """
    Test the response time.

    :param data_response: The response object.
    :return: None
    :raises AssertionError: If the elapsed time of the response exceeds 1 second.
    """
    assert data_response.elapsed.total_seconds() < 1
