from pydantic import BaseModel


class TranscriptionResponse(BaseModel):
    arquivo: str
    modelo: str
    idioma: str
    tempo_processamento_segundos: float
    texto: str