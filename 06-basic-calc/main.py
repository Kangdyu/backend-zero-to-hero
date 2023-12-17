from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class CalcResponse(BaseModel):
    result: int


@app.get("/sum")
def get_sum(a: int, b: int) -> CalcResponse:
    return CalcResponse(result=a + b)


@app.get("/mul", response_model=CalcResponse)
def get_mul(a: int, b: int):
    return {"result": a * b}
