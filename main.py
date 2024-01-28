from typing import Optional

from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/sound")
async def get_sound():
    return FileResponse("./audio/test.wav", media_type="audio/wav")