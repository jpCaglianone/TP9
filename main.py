from fastapi import FastAPI
import BancoRepository as br

app = FastAPI()

br.criacao_inicial()
# br.select_exercicio1()

@app.get("/")
async def root():
  return { "message": "Hello world" }


@app.get("/select/{nome_tabela}")
async def selectTabela(nome_tabela: str):
  #br.select_teste(nome_tabela)
  return { "message": f" {br.select_teste(nome_tabela)}" }

@app.get("/exercicio1")
async def exercicio1():
  return { "Resultado": f" {br.exercicio1()}!"}