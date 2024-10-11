import requests
import time  # Import time to measure execution duration


def get_project_info(uni):
    url = f"https://virtserver.swaggerhub.com/Columbia-Classes/ProjectInfoV3/1/projects?uni={uni}"

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


def call_api_three_times(uni):
    """Encapsulates the API call logic to call the API three times synchronously."""
    responses = []
    for i in range(3):
        print(f"Calling API attempt {i + 1}...")
        result = get_project_info(uni)
        responses.append(result)
    return responses


# Example usage:
def main():
    uni = 'dff9'

    # Start measuring time
    start_time = time.time()

    # Call API three times synchronously
    project_info_list = call_api_three_times(uni)

    # Calculate total execution time
    total_time = time.time() - start_time

    # Print all the responses
    for i, project_info in enumerate(project_info_list):
        print(f"Response {i + 1}: {project_info}")

    # Print total execution time
    print(f"Total execution time: {total_time:.2f} seconds")


# To run the program
if __name__ == "__main__":
    main()
