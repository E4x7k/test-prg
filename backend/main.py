from contextlib import asynccontextmanager

import joblib
from fastapi import FastAPI
from schemas import ClientData


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.model = joblib.load("model.pkl")
    yield


app = FastAPI(title='Test scoring app', lifespan=lifespan)



@app.post("/score")
def score(data: ClientData):
    features = [data.age, data.income, data.education, data.work, data.car]
    approved = not app.state.model.predict([features])[0].item()
    return {"approved": approved}