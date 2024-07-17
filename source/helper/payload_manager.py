#paylaod for all the request


def create_booking_payload():
    payload={
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
    return payload

def create_token():
    paylaod={
        "username": "admin",
        "password": "password123"
    }
    return paylaod

def put_booking_payload():
    payload={
            "firstname": "julie",
            "lastname": "Brown",
            "totalprice": 111,
            "depositpaid":False,
            "bookingdates": {
                "checkin": "2013-02-23",
                "checkout": "2014-10-23"
            },
            "additionalneeds": "Breakfast"
        }
    return payload