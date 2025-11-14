from fastapi import FastAPI, APIRouter

router_car = APIRouter(prefix="/api/cars", tags=["cars"])
router_train = APIRouter(prefix="/api/trains", tags=["trains"])

def get_start():
    return {"function": "start"}

def get_go():
    return {"function": "go"}

def get_back():
    return {"function": "back"}

def get_end():
    return {"function": "end"}

@router_car.get("/start")
def car_start_endpoint():
    return get_start()

@router_car.get("/go")
def car_go_endpoint():
    return get_go() 

@router_car.get("/back")
def car_back_endpoint():
    return get_back()

@router_car.get("/end")
def car_end_endpoint():
    return get_end()

@router_train.get("/start")
def train_start_endpoint():
    return get_start()

@router_train.get("/go")
def train_go_endpoint():
    return get_go()

@router_train.get("/back")
def train_back_endpoint():
    return get_back()

@router_train.get("/end")
def train_end_endpoint():
    return get_end()

app = FastAPI(docs_url="/api/docs", openapi_url="/api/openapi.json")
app.include_router(router_car)
app.include_router(router_train)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8888)