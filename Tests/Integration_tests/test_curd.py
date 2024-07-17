import pytest
import requests
from source.constants.api_constants import API_Constants
from source.helper.utilis import common_headers_json,common_token_headers_json
from source.helper.api_request_wrapper import post_request,put_request,patch_request,delete_request
from source.helper.payload_manager import create_booking_payload,create_token,put_booking_payload
from source.helper.common_verificatin import verify_response_should_not_be_none,verify_http_status_code,verify_key_is_not_null


class Testcurd():

    @pytest.fixture()
    def test_token_tc1(self):
        response=post_request(url=API_Constants.create_token(self),
                              auth=None,
                              payload=create_token(),
                              headers=common_headers_json(),
                              in_json=False
                              )
        verify_http_status_code(response,200)
        token=(response.json()["token"])
        verify_response_should_not_be_none(token)
        return token

    @pytest.fixture()
    def test_create_booking_tc2(self):
        response=post_request(url=API_Constants.create_booking_url(),
                              headers=common_headers_json(),
                              auth=None,
                              in_json=False,
                              payload=create_booking_payload()
                              )
        verify_http_status_code(response,expected_data=200)
        verify_key_is_not_null(response.json()["bookingid"])
        print(response.json()["bookingid"])
        bookingid=response.json()["bookingid"]
        return bookingid

    def test_update_booking_tc3(self,test_token_tc1,test_create_booking_tc2):
        # print(test_create_booking_tc2)
        # print(test_token_tc1)
        bookingid=test_create_booking_tc2
        response=put_request(url=API_Constants.put_patch_delete_get(bookingid),
                             headers=common_token_headers_json(),
                             auth=None,
                             in_json=False,
                             payload=put_booking_payload()
                             )
        verify_http_status_code(response,200)


    def test_delete_booking_tc4(self,test_token_tc1,test_create_booking_tc2):
        bookingid=test_create_booking_tc2
        response=put_request(url=API_Constants.put_patch_delete_get(bookingid),
                             headers=common_token_headers_json(),
                             auth=None,
                             in_json=False,
                             payload=None
                             )
        # verify_http_status_code(response,201)
        print(response.json())

    # def test_delete_booking(self, create_token, create_booking):  # Token and Booking ID from the Create Booking, Token
    #     bookindId = create_booking
    #     delete_url = APIConstants.url_create_booking() + "/" + str(bookindId)
    #
    #     response = put_requests(url=delete_url, headers=common_headers_for_put_delete_patch(), auth=None,
    #                             payload=None, in_json=False)
    #     print(response.json())


    # def test_delete_booking_tc4(self,test_token_tc1,test_create_booking_tc2):
    #     bookingid=test_create_booking_tc2
    #     response=p(url=API_Constants.put_patch_delete_get(bookingid),
    #                          headers=common_token_headers_json(),
    #                          auth=None,
    #                          in_json=False,
    #                          payload=put_booking_payload()
    #                          )
    #     verify_http_status_code(response,200)







