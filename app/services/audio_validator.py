from pathlib import Path
import av

from app.config import settings


class AudioValidator:


    def validar_tamanho(self, arquivo: Path):

        tamanho_mb = arquivo.stat().st_size / (1024 * 1024)

        if tamanho_mb > settings.MAX_AUDIO_SIZE_MB:
            raise Exception(
                f"Arquivo muito grande. "
                f"Máximo permitido: {settings.MAX_AUDIO_SIZE_MB} MB"
            )


    def validar_duracao(self, arquivo: Path):

        container = av.open(str(arquivo))

        duracao_segundos = container.duration / av.time_base

        container.close()

        duracao_minutos = duracao_segundos / 60


        if duracao_minutos > settings.MAX_AUDIO_DURATION_MINUTES:
            raise Exception(
                f"Áudio muito longo. "
                f"Máximo permitido: "
                f"{settings.MAX_AUDIO_DURATION_MINUTES} minutos"
            )


    def validar(self, arquivo: Path):

        self.validar_tamanho(arquivo)
        self.validar_duracao(arquivo)