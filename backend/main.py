import logging
import os
import pathlib
import sys
from contextlib import asynccontextmanager

import joblib
from dotenv import load_dotenv
from fastapi import FastAPI, status
from schemas import ClientData

load_dotenv()

logging.basicConfig(level=logging.INFO,
                                 format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
                                 datefmt='%Y-%m-%d %H:%M:%S',
                                 stream=sys.stdout
                                 )

logger = logging.getLogger(__name__)

if os.getenv('MODE') != 'DEV':
    logger.disabled = True

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Start application")
    BASE_DIR = pathlib.Path(__file__).parent.parent
    app.state.model = joblib.load(BASE_DIR / "model" / "model.pkl")
    logger.info("Model is loaded")
    yield
    logger.info("Start shutdown")

app = FastAPI(title='Test scoring app', lifespan=lifespan)



@app.post("/score", status_code=status.HTTP_200_OK, summary="Скоринг клиента")
def score(data: ClientData):
    features = [data.age, data.income, data.education, data.work, data.car]
    approved = not app.state.model.predict([features])[0].item()
    return {"approved": approved}