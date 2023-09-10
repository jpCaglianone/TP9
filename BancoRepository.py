import sqlite3 as sql
import os
import dados
import scriptsBanco as scripts

def criacao_inicial():
    try:
        conn = sql
        j = 0
        for i in scripts.nomesTabelas:
            # colocar a verificacao de arquivo existente
            conn = sql.connect(i)
            print(f"Tabela {i} criada")
            cursor = conn.cursor()
            conn.execute('BEGIN')
            cursor.execute(scripts.scriptsCriacao[j])
            print(f"Colunas inseridas em {i}")

            for row in scripts.scriptsInserts[j]['dado']:
                cursor.execute(scripts.scriptsInserts[j]['script'], row)
                print(f'linha inserida em {i}')

            print()
            j += 1
            conn.commit()

    except Exception as error:
        conn.rollback()
        print("Erro: " + str(error))

    finally:
        conn.close()

#
# f       or i in scripts.scriptsInserts:
#             for row in i['dado']:
#                 cursor.execute(i['script'], row)
#                 print("OK")
#         conn.commit()