from fastapi import FastAPI

from app.api.transcription import router as transcription_router


app = FastAPI(
    title="Reis AI",
    description="Serviço de inteligência artificial para transcrição de áudio",
    version="1.0.0"
)


app.include_router(transcription_router)


@app.get("/")
def home():
    return {
        "sistema": "Reis AI",
        "status": "online"
    }