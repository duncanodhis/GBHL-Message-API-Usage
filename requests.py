import requests

def register(firstname: str, surname: str, token: str):
    url = "http://52.59.33.40/web/api/register"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    data = {
        "firstname": firstname,
        "surname": surname
    }
    response = requests.post(url, headers=headers, data=data)
    
    # Create a structured JSON response
    json_response = {}
    json_response["status_code"] = response.status_code

    # Determine if the request was successful based on the status code
    if response.status_code == 200:
        json_response["result"] = "success"
        json_response["message"] = "Registration successful. Welcome, Agent Smith."
    else:
        json_response["result"] = "error"
        json_response["message"] = "Your request was made with invalid credentials."
        
    return json_response





def read(code: str, token: str):
    url = f"http://52.59.33.40/web/api/{code}"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(url, headers=headers)
    
    # Create a structured JSON response
    json_response = {}
    json_response["status_code"] = response.status_code

    # Determine if the request was successful based on the status code
    if response.status_code == 200:
        json_response["result"] = "success"
        json_response["message"] = "Data retrieval successful, Agent Smith."
        json_response["data"] = response.json()  # assuming the response contains JSON data
    else:
        json_response["result"] = "error"
        json_response["message"] = "Your request was made with invalid credentials."
        
    return json_response


token = "2XNVmuH2YVhYvVGgh4YkV9m6ph4c8CxMMX6UzeeDh7LJTmgdLk4Fz38QLwFt3sSY6BHkCeK8B3Jhgt23Q4dX6A3pmFRMGnJejwDg"
firstname = "John"
surname = "Doe"



# Register
response = register(firstname, surname, token)
print("Registration Response:")
print("==============================")
print(response)
print("\n\n")  


token = "2XNVmuH2YVhYvVGgh4YkV9m6ph4c8CxMMX6UzeeDh7LJTmgdLk4Fz38QLwFt3sSY6BHkCeK8B3Jhgt23Q4dX6A3pmFRMGnJejwDg"
code = "645b7935951fd"

# Read
print("Read Response:")
print("==============================")
response = read(code, token)
print(response)
