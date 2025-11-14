from fastapi import FastAPI, APIRouter

router = APIRouter(prefix="/intents", tags=["intents"])

def list_intents() -> dict:
    return ["greeting", "question", "answer", "feedback"]

@router.get("/")
def intents_endpoint():
    return {"intents": list_intents()}

app = FastAPI(docs_url="/api/docs", openapi_url="/api/openapi.json")
app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8888)