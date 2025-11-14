from typing import Iterable
import numpy as np
from fastapi import FastAPI

app = FastAPI(docs_url="/api/docs", openapi_url="/api/openapi.json")

def compute_stats(values: Iterable[float]):
    arr = np.array(values)
    return {
        "count": int(arr.size),
        "mean": float(arr.mean()),
        "std": float(arr.std(ddof=0)),
    }

@app.get("/stats/basic")
def stats_endpoint():
    sample_data = [10.0, 20.0, 30.0, 40.0, 50.0]
    return compute_stats(sample_data)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8888)