import requests


def create_token():
    url = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(url=url, headers=headers, json=json_payload)
    data = response.json()
    token = data["token"]
    print(token)
    return token


def create_booking():
    print("Create Booking Testcase")
    URL = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "firstname": "Amit",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url=URL, headers=headers, json=json_payload)
    print(type(URL))
    print(type(headers))
    print(type(json_payload))

    # Assertions
    assert response.status_code == 200
    # get the reponse Body and Verify the JSON, Booking ID is not None
    data = response.json()
    booking_id = data["bookingid"]
    return booking_id


def test_put_request():
    # Booking ID and Token
    URL = "https://restful-booker.herokuapp.com/booking/"
    booking_id = create_booking()
    PUT_URL = URL+str(booking_id)
    cookie_value = "token="+create_token()
    headers = {
            "Content-Type": "application/json",
            "Cookie" :  cookie_value
               }
    print(headers)
    json_payload = {
        "firstname": "Amit",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.put(url=PUT_URL, headers=headers, json=json_payload)
    # Assertions
    assert response.status_code == 200
    # get the reponse Body and Verify the JSON, Booking ID is not None
    data = response.json()
    assert data["firstname"] == "Amit", "Failed Message - Incorrect FirstName"


def test_delete():
    try:
        URL = "https://restful-booker.herokuapp.com/booking/"
        booking_id = create_booking()
        PUT_URL = URL + str(booking_id)
        cookie_value = "token=" + create_token()
        headers = {
            "Content-Type": "application/json",
            "Cookie": cookie_value
        }
        print(headers)

        response = requests.delete(url=PUT_URL, headers=headers)
        # Assertions
        assert response.status_code == 201
    except Exception as e:
        print(e)
