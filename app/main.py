from fastapi import FastAPI


app = FastAPI(
    title="Reis AI",
    description="Serviço de inteligência artificial para transcrição de áudio",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "sistema": "Reis AI",
        "status": "online"
    }