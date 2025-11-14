import pandas as pd
from fastapi import FastAPI

app = FastAPI(docs_url="/api/docs", openapi_url="/api/openapi.json")

CHAT_LOGS = pd.DataFrame(
    {
        "turn": [1, 2, 3, 4, 5],
        "speaker": ["user", "bot", "user", "bot", "user"],
        "intent": ["greeting", "welcome", "question", "answer", "feedback"]
    }
)

def filter_by_intent(intent: str) -> list[dict]:
    filtered = CHAT_LOGS[CHAT_LOGS["intent"] == intent]
    return filtered.to_dict(orient="records")

@app.get("/logs/filter/")
def filter_endpoint(intent: str):
    return {"intent": intent, "records": filter_by_intent(intent)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8888)