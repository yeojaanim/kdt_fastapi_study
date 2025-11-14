from fastapi import FastAPI

app = FastAPI(docs_url="/api/docs", openapi_url="/api/openapi.json")

def add_numbers(a: float, b: float):
    return {"sum": a + b, "difference": a - b}

@app.get("/math/add")
def add_endpoint(a: float, b: float):
    return add_numbers(a, b)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8888)