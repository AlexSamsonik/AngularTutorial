from requests import status_codes


def test_response_status_code(data_response):
    assert data_response.status_code == status_codes.ok


def test_successful_response(data_response_json):
    assert data_response_json.get("message") == "Hello FastAPI"


def test_response_data_type(data_response_json):
    assert isinstance(data_response_json, dict)


def test_message_key_exists(data_response_json):
    assert "message" in data_response_json


def test_message_value(data_response_json):
    assert data_response_json.get("message") == "Hello FastAPI"


def test_message_value_type(data_response_json):
    assert isinstance(data_response_json.get("message"), str)


def test_response_structure(data_response_json):
    assert set(data_response_json.keys()) == {"message"}


def test_response_content_type(data_response):
    assert data_response.headers.get("Content-Type") == "application/json"


def test_response_server_name(data_response):
    assert data_response.headers.get("server") == "uvicorn"


def test_response_time(data_response):
    assert data_response.elapsed.total_seconds() < 1
