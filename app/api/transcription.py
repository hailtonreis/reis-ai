from fastapi import APIRouter, UploadFile, File, HTTPException

from app.services.audio_validator import AudioValidator
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

        try:

            audio_validator.validar(caminho)

        except ValueError as erro:

            raise HTTPException(
                status_code=400,
                detail=str(erro)
            )

        resultado = whisper_service.transcrever(caminho)

        return {
            "success": True,
            "message": "Transcrição realizada com sucesso.",
            "data": {
                "arquivo": arquivo.filename,
                "modelo": "base",
                "idioma": resultado["idioma"],
                "tempo_processamento_segundos": resultado["tempo_processamento_segundos"],
                "estatisticas": resultado["estatisticas"],
                "texto": resultado["texto"]
            }
        }

    finally:

        remover_arquivo(caminho)