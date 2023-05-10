# Import necessary modules
import requests
import json

# Function to register user
def register(firstname: str, surname: str, token: str):
    # URL of the registration endpoint
    url = "http://3.123.16.12/web/api/register"
    
    # Prepare the headers for the request, including the bearer token for authentication
    headers = {
        "Authorization": f"Bearer {token}"
    }
    
    # Prepare the data to be sent with the request
    data = {
        "firstname": firstname,
        "surname": surname
    }
    
    # Send the POST request to the server
    response = requests.post(url, headers=headers, data=data)
    
    # If the response status code is not 200, raise an exception
    if response.status_code != 200:
        raise Exception(f"Request failed with status {response.status_code}")
        
    # Return the response in JSON format
    return response.json()

# Function to read messages
def read(code: str, token: str):
    # URL of the read endpoint
    url = f"http://3.123.16.12/web/api/code"
    
    # Prepare the headers for the request, including the bearer token for authentication
    headers = {
        "Authorization": f"Bearer {token}"
    }
    
    # Prepare the parameters to be sent with the request
    params = {
        "code": code
    }
    
    # Send the GET request to the server
    response = requests.get(url, headers=headers, params=params)
    
    # If the response status code is not 200, raise an exception
    if response.status_code != 200:
        raise Exception(f"Request failed with status {response.status_code}")
        
    # Return the response in JSON format
    return response.json()


# Set the necessary variables
token = "2XNVmuH2YVhYvVGgh4YkV9m6ph4c8CxMMX6UzeeDh7LJTmgdLk4Fz38QLwFt3sSY6BHkCeK8B3Jhgt23Q4dX6A3pmFRMGnJejwDg"
firstname = "John"
surname = "Doe"

# Call the register function and print the returned code
response = register(firstname, surname, token)
code = response.get('code', None)
if code:
    print(f"Registered successfully. Your code is: {code}")

# Call the read function and print the returned message
response = read(code, token)
message = response.get('message', None)
if message:
    print(f"Received message: {message}")
