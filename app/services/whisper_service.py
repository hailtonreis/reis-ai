import time

from faster_whisper import WhisperModel
from app.config import settings


class WhisperService:

    def __init__(self):
        self.model = WhisperModel(
            settings.WHISPER_MODEL,
            device="cpu",
            compute_type="int8"
        )

    def transcrever(self, arquivo):

        inicio = time.time()

        segments, info = self.model.transcribe(
            arquivo
        )

        texto = ""

        for segment in segments:
            texto += segment.text + " "

        fim = time.time()

        return {
            "texto": texto.strip(),
            "idioma": info.language,
            "tempo_processamento_segundos": round(
                fim - inicio,
                2
            )
        }