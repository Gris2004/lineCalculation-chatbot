from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Coordinates(BaseModel):
    X1: float | None = None
    Y1: float | None = None
    X2: float | None = None
    Y2: float | None = None


@app.get("/")
def root():
    return {
        "message": "Hola mundo"
    }


@app.post("/calculate")
def calculate(coordinates: Coordinates):
    return {
        "message": "Coordenadas recibidas correctamente.",
        "coordinates": {
            "X1": coordinates.X1,
            "Y1": coordinates.Y1,
            "X2": coordinates.X2,
            "Y2": coordinates.Y2
        }
    }
