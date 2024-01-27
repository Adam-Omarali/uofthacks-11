from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
async def root():
    return FileResponse("./audio/test.wav", media_type="audio/wav")