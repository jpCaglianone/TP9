from fastapi import FastAPI
import BancoRepository as br

app = FastAPI()

br.criacao_inicial()

# Default root endpoint
@app.get("/")
async def root():
  return { "message": "Hello world" }

# Example path parameter
@app.get("/name/{name}")
async def name(name: str):
  return { "message": f"Hello {name}" }