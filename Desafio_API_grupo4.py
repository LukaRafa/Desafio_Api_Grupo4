# Lucas Santos
# Maria Eduarda Fontana
# Maria Eduarda Góes
import random
import requests
import json
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/fraseCriptografada")
def criptografa():
    frase = buscar_mensagem()
    numero = random.randint(1,26)
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    fraseCriptografada = ''
    for a in frase:
        posição = alfabeto.find(a)
        if posição == -1:
            fraseCriptografada = fraseCriptografada + a
        else:
            nova_posição = posição + numero
            nova_posição = nova_posição % len(alfabeto)
            fraseCriptografada = fraseCriptografada + alfabeto[nova_posição:nova_posição+1]
        mensagem = {"frase":fraseCriptografada, "chave":numero}
    return mensagem

class Response(BaseModel):
    frase:str
    chave:int

@app.post("/fraseDescriptografada")
def descriptografa(body: Response):
    frase = body.frase
    chave = body.chave
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    fraseDescriptografada = ''
    for a in frase:
        posição = alfabeto.find(a)
        if posição == -1:
            fraseDescriptografada = fraseDescriptografada + a
        else:
            nova_posição = posição - chave
            nova_posição = nova_posição % len(alfabeto)
            fraseDescriptografada = fraseDescriptografada + alfabeto[nova_posição:nova_posição+1]
    return fraseDescriptografada

def buscar_mensagem():
    request = requests.get("http://dog-api.kinduff.com/api/facts")
    objetos = json.loads(request.text)
    dados   = objetos['facts']
    lst_str = str(dados)[2:-3]
    return lst_str


if __name__ == '__main__':
    buscar_mensagem()


