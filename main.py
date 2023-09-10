from fastapi import FastAPI
import BancoRepository as br

app = FastAPI()

br.criacao_inicial()


@app.get("/")
async def root():
  return { "message": "Hello world" }


@app.get("/select/{nome_tabela}")
async def selectTabela(nome_tabela: str):
  
  return { "message": f" {br.select_teste(nome_tabela)}" }