import sqlite3 as sql
import os
import dados
import scriptsBanco as scripts


def criacao_inicial():
  
    try:
      conn = sql
      for i in scripts.nomesTabelas:
        #colocar a verificacao de arquivo existente
        conn = sql.connect(i)
        
      for i in scripts.scriptsCriacao:
        cursor = conn.cursor()
        conn.execute('BEGIN')
        cursor.execute(i)
        
        for i in scripts.scriptsInserts:
            for row in i['dado']:
                cursor.execute(i['script'], row)
                print("ok!")
        conn.commit()
    except Exception as error:
      # conn.rollback()
      print("Erro: " + str(error))
    
    finally:
      conn.close()


def consulta_teste():
    for i in scripts.nomesTabelas:
      conn = sql.connect(i)
      cursor = conn.cursor()
      cursor.execute(f"SELECT * FROM {i}")
      rows = cursor.fetchall()
  
      for row in rows:
          print(row[1])
      conn.close()
    
