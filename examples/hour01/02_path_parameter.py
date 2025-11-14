from fastapi import FastAPI
app = FastAPI(docs_url="/api/docs", openapi_url="/api/openapi.json")

def greet_user(name: str):
    return {"message": f"Hello, {name}!"}

@app.get("/users/{name}")

def greet_endpoint(name: str):
    return greet_user(name)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8888)