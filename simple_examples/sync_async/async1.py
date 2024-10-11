import aiohttp
import asyncio
import time  # Import time to measure execution duration


async def get_project_info(uni):
    url = f"https://virtserver.swaggerhub.com/Columbia-Classes/ProjectInfoV3/1/projects?uni={uni}"

    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as response:
                response.raise_for_status()  # Check if the request was successful
                return await response.json()  # Return the JSON response
        except aiohttp.ClientResponseError as err:
            print(f"HTTP error occurred: {err}")
            return None
        except Exception as err:
            print(f"An error occurred: {err}")
            return None


async def call_api_three_times(uni):
    """Encapsulates the API call logic to call the API three times asynchronously."""
    tasks = [get_project_info(uni) for _ in range(3)]  # Create 3 tasks
    return await asyncio.gather(*tasks)  # Run tasks concurrently and gather results


# Example usage:
async def main():
    uni = 'dff9'

    # Start measuring time
    start_time = time.time()

    # Call API three times asynchronously
    project_info_list = await call_api_three_times(uni)

    # Calculate total execution time
    total_time = time.time() - start_time

    # Print all the responses
    for i, project_info in enumerate(project_info_list):
        print(f"Response {i + 1}: {project_info}")

    # Print total execution time
    print(f"Total execution time: {total_time:.2f} seconds")


# To run the async function
if __name__ == "__main__":
    asyncio.run(main())
