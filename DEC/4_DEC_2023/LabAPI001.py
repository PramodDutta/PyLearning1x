# API
# Request Lib
import requests


# Make a GET, POST, PUT , PATCH and DELETE and verify.
# HTTP Methods

def main():
    # GET - URL
    response_body = requests.get("https://restful-booker.herokuapp.com/booking/1421")
    if response_body.status_code == 200:
        print("TC#1 - GET request is successfully")
    else:
        print("TC#1 - GET request is Not successfully")

# To make an API Testing Req.
# url, auth, headers, cookies, data (payload), json, file

# Validate in API Testing
# response, headers, statuscode,responseTime, JSON Schema Validation




if __name__ == "__main__":
    main()
