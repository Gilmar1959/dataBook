import os
import dotenv
import requests

dotenv.load_dotenv()

def analise_sentimento(texto: str) -> str:
    CHAVE_API = os.getenv("CHAVE_API", None)
    modelo_engine = "gpt-3.5-turbo-instruct"
    comando = f"Responda em uma única palavra, sendo positivo, negativo ou neutro o sentimento contido no seguinte texto: '{texto}'"

    cabecalho = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {CHAVE_API}"
    }

    dados = {
        "prompt": comando,
        "temperature": 0.7,
        "max_tokens": 50,
        "n": 1,
        "stop": None,
    }

    resposta = requests.post(
        f"https://api.openai.com/v1/engines/{modelo_engine}/completions",
        headers=cabecalho,
        json=dados
    )

    return resposta.json()["choices"][0]["text"].strip().lower()