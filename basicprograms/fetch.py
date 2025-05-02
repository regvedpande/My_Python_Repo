import requests

def fetch_data_from_api(url):
    try:
        # Make a GET request to the API
        response = requests.get(url)

        # Raise an exception if the request was unsuccessful
        response.raise_for_status()

        # Parse the JSON response
        data = response.json()

        # Print the data
        print(data)

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

# Example usage with a public API
api_url = "https://jsonplaceholder.typicode.com/posts/1"
fetch_data_from_api(api_url)
