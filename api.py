from fastapi import FastAPI
from pydantic import BaseModel


class User_input(BaseModel):
    x: int
    y: int


app = FastAPI()

@app.post("/calculate")
def operate(input:User_input):
    y, x = input.y, input.x
    return y*x
