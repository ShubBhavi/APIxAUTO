import pytest
import requests
import  json
from source.constants.api_constants import API_Constants
from source.helper.utilis import common_headers_json
from source.helper.api_request_wrapper import post_request
from source.helper.payload_manager import create_booking_payload
from source.helper.common_verificatin import verify_response_should_not_be_none,verify_http_status_code
from jsonschema import validate
from jsonschema.exceptions import ValidationError

class Test_cases(object):

    def test_create_booking_tc1(self):
        #url,headers,payload
        response= post_request(url=API_Constants.create_booking_url(), auth=None, headers=common_headers_json(),payload=create_booking_payload(),in_json=False)
        print(response)
        verify_response_should_not_be_none(response.json()["bookingid"])
        verify_http_status_code(response,200)
        response_json=response.json()
        schema={
    "$schema": "https://json-schema.org/draft/2019-09/schema",
    "$id": "http://example.com/example.json",
    "type": "object",
    "default": {},
    "title": "Root Schema",
    "required": [
        "bookingid",
        "booking"
    ],
    "properties": {
        "bookingid": {
            "type": "integer",
            "default": 0,
            "title": "The bookingid Schema",
            "examples": [
                1290
            ]
        },
        "booking": {
            "type": "object",
            "default": {},
            "title": "The booking Schema",
            "required": [
                "firstname",
                "lastname",
                "totalprice",
                "depositpaid",
                "bookingdates",
                "additionalneeds"
            ],
            "properties": {
                "firstname": {
                    "type": "string",
                    "default": "",
                    "title": "The firstname Schema",
                    "examples": [
                        "Shubham"
                    ]
                },
                "lastname": {
                    "type": "string",
                    "default": "",
                    "title": "The lastname Schema",
                    "examples": [
                        "Brown"
                    ]
                },
                "totalprice": {
                    "type": "integer",
                    "default": 0,
                    "title": "The totalprice Schema",
                    "examples": [
                        111
                    ]
                },
                "depositpaid": {
                    "type": "boolean",
                    "default": False,
                    "title": "The depositpaid Schema",
                    "examples": [
                        True
                    ]
                },
                "bookingdates": {
                    "type": "object",
                    "default": {},
                    "title": "The bookingdates Schema",
                    "required": [
                        "checkin",
                        "checkout"
                    ],
                    "properties": {
                        "checkin": {
                            "type": "string",
                            "default": "",
                            "title": "The checkin Schema",
                            "examples": [
                                "2013-02-23"
                            ]
                        },
                        "checkout": {
                            "type": "string",
                            "default": "",
                            "title": "The checkout Schema",
                            "examples": [
                                "2014-10-23"
                            ]
                        }
                    },
                    "examples": [{
                        "checkin": "2013-02-23",
                        "checkout": "2014-10-23"
                    }]
                },
                "additionalneeds": {
                    "type": "string",
                    "default": "",
                    "title": "The additionalneeds Schema",
                    "examples": [
                        "Breakfast"
                    ]
                }
            },
            "examples": [{
                "firstname": "Shubham",
                "lastname": "Brown",
                "totalprice": 111,
                "depositpaid": True,
                "bookingdates": {
                    "checkin": "2013-02-23",
                    "checkout": "2014-10-23"
                },
                "additionalneeds": "Breakfast"
            }]
        }
    },
    "examples": [{
        "bookingid": 1290,
        "booking": {
            "firstname": "Shubham",
            "lastname": "Brown",
            "totalprice": 111,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2013-02-23",
                "checkout": "2014-10-23"
            },
            "additionalneeds": "Breakfast"
        }
    }]
}



        try:
            validate(instance=response_json,schema=schema)
        except ValidationError as error:
            print(error.message)
