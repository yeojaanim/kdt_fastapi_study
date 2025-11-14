from fastapi import FastAPI

app = FastAPI(docs_url="/api/docs", openapi_url="/api/openapi.json")

COURSE_TOPICS = ["fastapi-intro", "http-basics", "json", "uvicorn"]
def get_course_topics():
    return {"topics": COURSE_TOPICS, "count": len(COURSE_TOPICS)}
@app.get("/course/topics")
def topics_endpoint():
    return get_course_topics()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8888)