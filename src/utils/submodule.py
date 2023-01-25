import requests
import json

class ex_class:
    def __init__(self, api_key):
        self.api_key = api_key
        
    def sub_def(self, arg_1, arg_2):
        # Build the API request URL
        url = f"https://www.alphavantage.co/query?function=SECTOR&apikey={self.api_key}&region=US"

        # Make the API request
        response = requests.get(url)

        # Parse the JSON response
        data = json.loads(response.text)

        print(data)
        
        # Extract the performance metrics for the specified industry and sub-industry
        print(self.api_key)
        print(arg_1)
        print(arg_2)
