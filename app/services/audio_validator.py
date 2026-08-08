from pathlib import Path
import av

from app.config import settings


class AudioValidator:

    def validar_tipo(self, arquivo: Path):

        extensao = arquivo.suffix.lower()

        if extensao not in settings.ALLOWED_EXTENSIONS:
            raise ValueError(
                "Tipo de arquivo não suportado. "
                "Formatos aceitos: MP3, MP4, WAV e M4A."
            )

    def validar_tamanho(self, arquivo: Path):

        tamanho_mb = arquivo.stat().st_size / (1024 * 1024)

        if tamanho_mb > settings.MAX_AUDIO_SIZE_MB:
            raise ValueError(
                f"Arquivo muito grande. "
                f"Máximo permitido: {settings.MAX_AUDIO_SIZE_MB} MB"
            )

    def validar_duracao(self, arquivo: Path):

        try:
            container = av.open(str(arquivo))

            duracao_segundos = container.duration / av.time_base

            container.close()

        except Exception:
            raise ValueError(
                "Arquivo inválido ou corrompido. "
                "Não foi possível identificar um áudio ou vídeo válido."
            )

        duracao_minutos = duracao_segundos / 60

        if duracao_minutos > settings.MAX_AUDIO_DURATION_MINUTES:
            raise ValueError(
                f"Áudio muito longo. "
                f"Máximo permitido: "
                f"{settings.MAX_AUDIO_DURATION_MINUTES} minutos"
            )

    def validar(self, arquivo: Path):

        self.validar_tipo(arquivo)
        self.validar_tamanho(arquivo)
        self.validar_duracao(arquivo)
