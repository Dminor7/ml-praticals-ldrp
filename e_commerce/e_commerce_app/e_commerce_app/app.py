from fastapi import FastAPI
from pydantic import BaseModel
import typing as t

app = FastAPI()

class Request(BaseModel):
    browser: str
    channelGrouping: str
    operatingSystem: str
    deviceCategory: t.Literal["desktop","mobile","tablet"]
    continent: str
    country: str
    source: str
    medium: str

@app.post("/products")
def read_root(request: Request):
    
    return request
