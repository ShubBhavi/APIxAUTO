import pytest
import requests
import  json
from source.constants.api_constants import API_Constants
from source.helper.utilis import common_headers_json
from source.helper.api_request_wrapper import post_request
from source.helper.payload_manager import create_booking_payload
from source.helper.common_verificatin import verify_response_should_not_be_none,verify_http_status_code


class Test_cases(object):

    def test_create_booking_tc1(self):
        #url,headers,payload
        response= post_request(url=API_Constants.create_booking_url(), auth=None, headers=common_headers_json(),payload=create_booking_payload(),in_json=False)
        print(response)
        verify_response_should_not_be_none(response.json()["bookingid"])
        verify_http_status_code(response,200)

    def test_empty_payload_tc2(self):
        # url,headers,payload
        response = post_request(url=API_Constants.create_booking_url(), auth=None, headers=common_headers_json(),payload={}, in_json=False)
        verify_http_status_code(response, 500)



