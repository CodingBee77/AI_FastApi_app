from typing import Union
import io

from model import model_pipeline
from fastapi import FastAPI, UploadFile

from PIL import Image

from pydantic import BaseModel


class Answer(BaseModel):
    answer: str | None = None


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/ask_question")
def ask(text: str, image: UploadFile):
    content = image.file.read()
    image = Image.open(image.file)
    result = model_pipeline(text=text, image=image)
    return Answer(answer=result)
