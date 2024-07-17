##READ THE CSV FILE OR EXCEL FILE
##CREATE A FUNCTION CREATE_TOKEN WHICH CAN TAKE VALUES FROM THE EXCEL FILE
##VERIFY THE EXCPECTED RESULTS

import requests
import pytest
from source.constants.api_constants import API_Constants
from source.helper.utilis import common_headers_json
#read the excel file -openpyxl
import openpyxl

#step 1 read the file and put the content on list []

def read_credentials_from_excel(file_path):
    credentials=[]
    workbook=openpyxl.load_workbook()
    sheet=workbook.active

    for row in sheet.iter_rows(min_row=2,values_only=True):
        username,password=row
        credentials.append({"username":username,"password":password})

        return credentials


def make_request_auth(username,password):
    payload={
        "username":username,
        "password":password

    }
    response=requests.post(url=API_Constants.create_token(),headers=common_headers_json(),json=payload)
    return response

# def test_post_create_token():
#     file_path=r"C:\Users\SHUBHAM\PycharmProjects\pythonAPIautomation\Tests\DataDrivenTesting\TestDdt.xlsx"
#     credentials=read_credentials_from_excel(file_path)
#
#     for user_cred in credentials:
#         username=user_cred["username"]
#         password=user_cred["password"]
#         print(username,password)
#         response=make_request_auth(username,password)
#         print(response)

#alternative method

@pytest.mark.parametrize("user_cred",read_credentials_from_excel(r"C:\Users\SHUBHAM\PycharmProjects\pythonAPIautomation\Tests\DataDrivenTesting\testddt.xlsx"))
def test_post_create_token(user_cred):

        username=user_cred["username"]
        password=user_cred["password"]
        print(username,password)
        response=make_request_auth(username,password)
        print(response)
