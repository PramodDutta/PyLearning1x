import requests


def main():
    id = "538"
    url = "https://restful-booker.herokuapp.com/booking/"
    full_url = url + id
    print(full_url)
    response_body = requests.get(full_url)
    assert response_body.status_code == 200  # If sc != 200 it error, else it will not give error

    data = response_body.json()
    print(type(data))

    # Assertions

    # Verification of Keys
    assert 'firstname' in data, "Incorrect firstName"
    assert 'lastname' in data, "LastName key is present"

    # Verification of Data
    assert data["firstname"] == "Josh", "Incorrect  FirstName is Amit"
    assert data["lastname"] == "Allen", "Incorrect LastName"
    assert data["bookingdates"]["checkin"] == "2018-01-01", "Incorrect Message"


if __name__ == '__main__':
    main()
