#veriffy the status code
#http status code
#key is not null
#verify headers
#data verification
#json schema


def verify_http_status_code(response,expected_data):
    assert response.status_code == expected_data,"excepted status code"+str(expected_data)


def verify_key_is_not_null(key):
    assert key is not None,"key is not null"+key
    assert key>0, "key is greater than zero"

def verify_response_should_not_be_none(key):
    assert key is not None

def verify_time():
    pass
