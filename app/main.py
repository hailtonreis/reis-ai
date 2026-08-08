from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from app.api.transcription import router as transcription_router


app = FastAPI(
    title="Reis AI",
    description="Serviço de inteligência artificial para transcrição de áudio",
    version="1.0.0"
)

app.add_middleware(
     CORSMiddleware,
     allow_origins=[
         "http://localhost:4200",
         "https://hailtonreis.tech"
    ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
)


app.include_router(transcription_router)


@app.get("/")
def home():
    return {
        "sistema": "Reis AI",
        "status": "online"
    }