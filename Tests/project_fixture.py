import pytest

from source.constants.api_constants import API_Constants
from source.helper.api_request_wrapper import post_request
from source.helper.common_verificatin import verify_response_should_not_be_none, verify_http_status_code, \
    verify_key_is_not_null
from source.helper.payload_manager import create_booking_payload, create_token
from source.helper.utilis import common_headers_json


@pytest.fixture()
def token_tc1(self):
    response = post_request(url=API_Constants.create_token(self),
                            auth=None,
                            payload=create_token(),
                            headers=common_headers_json(),
                            in_json=False
                            )
    verify_http_status_code(response, 200)
    token = (response.json()["token"])
    verify_response_should_not_be_none(token)
    return token


@pytest.fixture()
def create_booking_tc2(self):
    response = post_request(url=API_Constants.create_booking_url(),
                            headers=common_headers_json(),
                            auth=None,
                            in_json=False,
                            payload=create_booking_payload()
                            )
    verify_http_status_code(response, expected_data=200)
    verify_key_is_not_null(response.json()["bookingid"])
    print(response.json()["bookingid"])
    bookingid = response.json()["bookingid"]
    return bookingid
