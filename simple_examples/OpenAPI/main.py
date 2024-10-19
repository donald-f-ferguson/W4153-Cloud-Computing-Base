from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import uvicorn

app = FastAPI()

# In-memory storage for courses
courses_db = {}

# Pydantic model for CourseInfo
class CourseInfo(BaseModel):
    course_id: str
    section_number: str
    semester: str
    year: int

# GET: Retrieve course info by course_id and section_number
@app.get("/courses/{course_id}/sections/{section_number}", response_model=CourseInfo)
def get_course(course_id: str, section_number: str):
    course_key = f"{course_id}-{section_number}"
    if course_key not in courses_db:
        raise HTTPException(status_code=404, detail="Course not found")
    return courses_db[course_key]

# POST: Create a new course
@app.post("/courses", response_model=CourseInfo, status_code=201)
def create_course(course: CourseInfo):
    course_key = f"{course.course_id}-{course.section_number}"
    if course_key in courses_db:
        raise HTTPException(status_code=400, detail="Course with this ID and section already exists")
    courses_db[course_key] = course
    return course

# PUT: Update existing course info
@app.put("/courses/{course_id}/sections/{section_number}", response_model=CourseInfo)
def update_course(course_id: str, section_number: str, course: CourseInfo):
    course_key = f"{course_id}-{section_number}"
    if course_key not in courses_db:
        raise HTTPException(status_code=404, detail="Course not found")
    if course.course_id != course_id or course.section_number != section_number:
        raise HTTPException(status_code=400, detail="Course ID or section in path and body do not match")
    courses_db[course_key] = course
    return course

# DELETE: Remove a course by course_id and section_number
@app.delete("/courses/{course_id}/sections/{section_number}", status_code=204)
def delete_course(course_id: str, section_number: str):
    course_key = f"{course_id}-{section_number}"
    if course_key not in courses_db:
        raise HTTPException(status_code=404, detail="Course not found")
    del courses_db[course_key]
    return {"detail": "Course deleted successfully"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8011)
