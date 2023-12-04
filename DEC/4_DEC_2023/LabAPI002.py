import requests

response_body = requests.get("https://restful-booker.herokuapp.com/booking/1421")
print(response_body.text)
print(response_body.headers)

# Verify ?
# Assertion -> Verify the Expected Result with the Actual Result
# Status Code ER ->  200
# AR -> 200
#
# iF id = 1420 -
# ER = 404
# AR - 404