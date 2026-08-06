from app.services.audio_validator import AudioValidator

from fastapi import APIRouter, UploadFile, File

from app.services.whisper_service import WhisperService
from app.utils.file_utils import salvar_arquivo, remover_arquivo


router = APIRouter(
    prefix="/transcription",
    tags=["Transcrição"]
)

whisper_service = WhisperService()
audio_validator = AudioValidator()


@router.post("")
async def transcrever_audio(
    arquivo: UploadFile = File(...)
):

    caminho = salvar_arquivo(arquivo)

    try:

        audio_validator.validar(caminho)

        resultado = whisper_service.transcrever(caminho)

        return {
            "arquivo": arquivo.filename,
            "modelo": "base",
            "idioma": resultado["idioma"],
            "tempo_processamento_segundos": resultado["tempo_processamento_segundos"],
            "texto": resultado["texto"]
        }

    finally:

        remover_arquivo(caminho)