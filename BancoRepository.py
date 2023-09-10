import sqlite3 as sql
import dados
import scriptsBanco as scripts

def criacao_inicial():
    try:
        for i, nome in enumerate(scripts.nomesTabelas):
            # Conectar ao banco de dados
            conn = sql.connect(nome + ".db")  # Adicione a extensão .db ao nome do banco de dados
            cursor = conn.cursor()
            conn.execute('BEGIN')
            
            # Criar tabela
            cursor.execute(scripts.scriptsCriacao[i])
            
            # Inserir dados
            for row in scripts.scriptsInserts[i]['dado']:
                cursor.execute(scripts.scriptsInserts[i]['script'], row)
              
            conn.commit()
            conn.close()

    except Exception as error:
        conn.rollback()
        print("Erro: " + str(error))

def select_teste(nome):
    resultado = ""
    conn = sql.connect(nome + ".db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {nome}")
    rows = cursor.fetchall()    
  
    for row in rows:
        resultado += " ".join(map(str, row)) + " - "
    
    conn.close()

    return resultado
