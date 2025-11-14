from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

app = FastAPI(docs_url="/api/docs", openapi_url="/api/openapi.json")

class TooShortError(ValueError):
    """Custom exception for texts that are too short."""

def validate_length(text: str) -> str:
    if len(text) < 3:
        raise TooShortError("Text is too short")
    return text

@app.exception_handler(TooShortError)
async def short_error_hardler(_: Request, exc: TooShortError) -> JSONResponse:
    return JSONResponse(
        status_code=422,
        content={"detail": str(exc)}
    )

@app.get("/validate/")
def validate_endpoint(text: str) -> dict:
    return {"validated": validate_length(text)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8888)