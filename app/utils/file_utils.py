from pathlib import Path
import shutil

from fastapi import UploadFile


TEMP_DIR = Path("temp")
TEMP_DIR.mkdir(exist_ok=True)


def salvar_arquivo(upload_file: UploadFile) -> Path:
    destino = TEMP_DIR / upload_file.filename

    with open(destino, "wb") as buffer:
        shutil.copyfileobj(upload_file.file, buffer)

    return destino


def remover_arquivo(caminho: Path):
    if caminho.exists():
        caminho.unlink()