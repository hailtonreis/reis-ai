class Settings:

    # Whisper
    WHISPER_MODEL = "base"
    LANGUAGE = "pt"

    # Limites de upload
    MAX_AUDIO_SIZE_MB = 300
    MAX_AUDIO_DURATION_MINUTES = 150

    # Formatos de arquivo permitidos
    ALLOWED_EXTENSIONS = {
        ".mp3",
        ".mp4",
        ".wav",
        ".m4a"
    }


settings = Settings()