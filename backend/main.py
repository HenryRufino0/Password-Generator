from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import string
import secrets

app = FastAPI()

# Permitir acesso cross-origin para o frontend (necessário em ambiente local)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ajuste para segurança em produção
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/generate-password")
def generate_password(
    length: int = Query(12, ge=4, le=64),  # Tamanho padrão da senha (mín:4, máx:64)
    uppercase: bool = True,
    lowercase: bool = True,
    digits: bool = True,
    special_chars: bool = True,
):
    """
    Endpoint para gerar senhas seguras.

    Parâmetros:
    - length (int): Tamanho da senha.
    - uppercase (bool): Incluir letras maiúsculas.
    - lowercase (bool): Incluir letras minúsculas.
    - digits (bool): Incluir números.
    - special_chars (bool): Incluir caracteres especiais.

    Retorno:
    - JSON contendo a senha gerada.
    """

    # Montando conjunto de caracteres
    alphabet = ""
    if uppercase:
        alphabet += string.ascii_uppercase
    if lowercase:
        alphabet += string.ascii_lowercase
    if digits:
        alphabet += string.digits
    if special_chars:
        alphabet += string.punctuation

    # Verifica se ao menos uma categoria foi escolhida
    if not alphabet:
        return {"error": "Selecione ao menos um tipo de caractere."}

    # Gerando senha segura
    password = ''.join(secrets.choice(alphabet) for _ in range(length))

    return {"password": password}
