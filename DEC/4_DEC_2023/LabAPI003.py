import requests


def main():
    id = "1421"
    url = "https://restful-booker.herokuapp.com/booking/"
    full_url = url+id
    print(full_url)
    response_body = requests.get(full_url)
    assert response_body.status_code == 200 # If sc != 200 it error, else it will not give error


if __name__ == '__main__':
    main()
