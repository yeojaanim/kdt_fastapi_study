from fastapi import FastAPI

app = FastAPI(
    docs_url="/api/docs",
    openapi_url="/api/openapi.json",
    title="Voice Chatbot API",
    description="음성 챗봇 엔드포인트를 실습용으로 제공합니다.",
    version="0.1.0",
    contact={"name": "강의자", "email": "instructor@example.com"}
)

@app.get("/docs-check")
def docs_check():
    """Swagger UI에서 확인할 간단한 응답"""
    return {"message": "Open the /docs page to see this endpoint"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8888)