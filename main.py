from fastapi import FastAPI, status
from pydantic import BaseModel
from typing import List

app = FastAPI(title='API de receitas')

class Receita(BaseModel):
    nome: str
    ingredientes: List[str]
    modo_de_preparo: str

receitas: List[Receita] = []

'''
receitas = [
    {
        'nome': 'brownie',
        'ingredientes': ['3 ovos', '6 colheres de açúcar']
        'modo_de_preparo: ...'
    },
]
'''


@app.get("/")
def hello():
    return{"title": "Livro de receitas"}

@app.get("/receitas/")
def get_todas_receitas():
    return receitas

@app.get("/receitas/{nome_receita}")
def get_receita(nome_receita: str):
    for receita in receitas:
        if receita["nome"] == nome_receita:
            return receita
    return {"erro": "receita não encontrada"}


@app.post("/receitas", response_model=Receita, status_code=status.HTTP_201_CREATED)
def criar_receita(dados: Receita):

    nova_receita = dados
    
    receitas.append(nova_receita)

    return nova_receita


