from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class CalcResponse(BaseModel):
    result: int


"""
NOTE: response_model과 explicit return type 모두 같은 결과를 반환함
editor/type tool support를 위해 return type을 사용하는 쪽이 권장되는 것으로 보임
SEE: https://fastapi.tiangolo.com/tutorial/response-model/#return-type-and-data-filtering
"""


@app.get("/sum")
def get_sum(a: int, b: int) -> CalcResponse:
    return CalcResponse(result=a + b)


@app.get("/mul", response_model=CalcResponse)
def get_mul(a: int, b: int):
    return CalcResponse(result=a * b)
