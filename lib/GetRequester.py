
import json

import requests

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status() 
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

    def load_json(self):
        response_body = self.get_response_body()
        if response_body:
            try:
                json_data = json.loads(response_body)  
            except json.JSONDecodeError as e:
                print(f"Failed to parse JSON: {e}")
                return None
        else:
            return None


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/posts/1"
    requester = GetRequester(url)

 
    response_body = requester.get_response_body()
    print("Response Body:")
    print(response_body)


    json_data = requester.load_json()
    if json_data:
        print("\nJSON Data:")
        print(json_data)
