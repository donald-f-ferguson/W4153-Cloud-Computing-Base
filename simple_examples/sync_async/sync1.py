import json

import requests
import time  # Import time to measure execution duration

urls = [
    {"rel": "courses", "href": "https://virtserver.swaggerhub.com/Columbia-Classes/CourseInfo/1.0/courses?uni=ab123"},
    {"rel": "teams", "href": "https://virtserver.swaggerhub.com/Columbia-Classes/TeamsInfo/1.0/teams?uni=ab1234"},
    {"rel": "person", "href": "https://virtserver.swaggerhub.com/Columbia-Classes/PersonInfo/1.0/persons/dff9"}
]


def call_get(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        return response.json()  # Return the JSON response
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
        return None
    except Exception as err:
        print(f"An error occurred: {err}")
        return None


def call_get_urls(urls):

    result = {}

    for u in urls:
        r = call_get(u["href"])
        t = r.get(u["rel"],r)
        result[u["rel"]] = t

    return result

# Example usage:
def main():

    # Start measuring time
    start_time = time.time()

    # Call API three times synchronously
    full_result = call_get_urls(
        urls
    )

    # Calculate total execution time
    total_time = time.time() - start_time

    # Print all the responses
    print("The full response = \n",
          json.dumps(full_result, indent=2))

    # Print total execution time
    print(f"Total execution time: {total_time:.2f} seconds")


# To run the program
if __name__ == "__main__":
    main()
