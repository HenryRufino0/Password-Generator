import fastapi
from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import string
import secrets

app = FastAPI()

# Configuração do CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, substitua por domínios específicos
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/generate-password")
def generate_password(
    length: int = Query(12, ge=4, le=64),
    uppercase: bool = True,
    lowercase: bool = True,
    digits: bool = True,
    special_chars: bool = True,
):
    """
    Endpoint para gerar senhas seguras.
    """

    # Conjunto de caracteres disponíveis
    char_sets = {
        "uppercase": string.ascii_uppercase if uppercase else "",
        "lowercase": string.ascii_lowercase if lowercase else "",
        "digits": string.digits if digits else "",
        "special_chars": string.punctuation if special_chars else ""
    }

    # Filtra apenas os conjuntos selecionados
    selected_char_sets = [chars for chars in char_sets.values() if chars]

    if not selected_char_sets:
        raise HTTPException(status_code=400, detail="Selecione ao menos um tipo de caractere.")

    # Garante que pelo menos um caractere de cada tipo escolhido esteja na senha
    password = [secrets.choice(chars) for chars in selected_char_sets]

    # Preenche o restante da senha aleatoriamente
    all_chars = "".join(selected_char_sets)
    password += [secrets.choice(all_chars) for _ in range(length - len(password))]

    # Embaralha a senha para não ficar previsível
    secrets.SystemRandom().shuffle(password)

    return {"password": "".join(password)}


"To activate the server: uvicorn main:app --reload"