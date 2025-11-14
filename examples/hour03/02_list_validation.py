from typing import List
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(docs_url="/api/docs", openapi_url="/api/openapi.json")

class BatchScores(BaseModel):
    scores: List[float] = Field([0.1,0.2,0.3,0.4], description="0~1 사이의 점수")

def summarize_scores(payload: BatchScores) -> dict:
    if not payload.scores:
        return {"count": 0, "mean": None, "stddev": None}
    total = sum(payload.scores)
    count = len(payload.scores)
    return {
        "count": count,
        "mean": total / count,
        "max": max(payload.scores)
    }

@app.post("/scores/summary")
def scores_endpoint(payload: BatchScores):
    return summarize_scores(payload)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8888)