from fastapi import FastAPI, Request
import uvicorn
import logging
import time

# Initialize the FastAPI app
app = FastAPI()

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Middleware to log requests before and after
@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"Request: {request.method} {request.url}")

    # Log before the request is processed
    start_time = time.time()

    # Call the next process in the pipeline
    response = await call_next(request)

    # Log after the request is processed
    process_time = time.time() - start_time
    logger.info(f"Response status: {response.status_code} | Time: {process_time:.4f}s")

    return response


# Define a simple API path
@app.get("/projects/{project_id}")
async def get_project(project_id: int):
    # Dummy project info
    project_info = {
        "project_id": project_id,
        "name": f"Project {project_id}",
        "description": f"Details of project {project_id}"
    }
    return project_info


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
