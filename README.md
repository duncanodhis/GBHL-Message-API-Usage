# GBHL Message API Usage

This Python script uses the GBHL Message API to register a user and read a message.

## Prerequisites

Ensure you have Python installed on your system. The `requests` library is also required. You can install it using pip:

```shell
pip install requests

Usage

Open the Python script.
In the register and read functions, use  http://3.123.16.12/web/api/register and http://3.123.16.12/web/api/code or you can replace with the actual API endpoints, if different.
Replace the token variable with your actual token or use the one provided.
if need be ,replace firstname and surname variables with the actual first name and surname you want to 

register.
Run the script in a Python environment.


After running the script, it will register the user with the provided first name and surname and then read a message using the returned code from the registration process.

The script prints the code returned from the registration process and the message returned from the read process to the console.
