import sqlite3 as sql
import dados
import scriptsBanco as scripts
import os

nome_banco = "T_Geral.bd"

def criacao_inicial():
  if not os.path.isfile(nome_banco):
    try:
        conn = sql.connect(nome_banco)
        for i, nome in enumerate(scripts.nomesTabelas):
           
            cursor = conn.cursor()
            conn.execute('BEGIN')
            
            cursor.execute(scripts.scriptsCriacao[i])

            for row in scripts.scriptsInserts[i]['dado']:
                cursor.execute(scripts.scriptsInserts[i]['script'], row)
              
            conn.commit()
            
    except Exception as error:
        conn.rollback()
        print("Erro: " + str(error))
      
    finally: 
      conn.close()


def select_teste(nome):
    resultado = ""

    conn = sql.connect(nome_banco)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM " + nome)
    rows = cursor.fetchall()    
    for row in rows:
        resultado += " ".join(map(str, row)) + " - "
    
    conn.close()
    return resultado

def execSelects(script):
    conn = sql.connect(nome_banco)
    cursor = conn.cursor()
    cursor.execute(script)
    rows = cursor.fetchall()
    conn.close()
    return rows

def exercicio1():
    return execSelects(scripts.script_exercicio1)

def exercicio2():
    return execSelects(scripts.script_exercicio2)

def exercicio3():
    return execSelects(scripts.script_exercicio3)