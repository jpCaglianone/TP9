import dados

nomesTabelas = ["T_Departamento",
               "T_Tecnico",
               "T_Prioridade",
               "T_Usuario",
                "T_Ativo",
               "T_Chamado"]

scriptCriacao_tChamado = '''
    CREATE TABLE IF NOT EXISTS T_Chamado (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        descricao VARCHAR(100),
        data_Fechamento DATETIME,
        data_abertura DATETIME,
        status VARCHAR(20),
        id_Tecnico INTEGER,
        id_Usuario INTEGER,
        id_Prioridade INTEGER,
        id_Ativos INTEGER,
        FOREIGN KEY (id_Tecnico) REFERENCES T_Tecnico(id),
        FOREIGN KEY (id_Usuario) REFERENCES T_Usuario(id),
        FOREIGN KEY (id_Prioridade) REFERENCES T_Prioridade(id),
        FOREIGN KEY (id_Ativos) REFERENCES T_Ativos(id)
    )
'''


scriptCriacao_tDepartamento =  '''
              CREATE TABLE IF NOT EXISTS T_Departamento(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                descricao VARCHAR(50)
              )
'''



scriptCriacao_tTecnico =  '''
              CREATE TABLE IF NOT EXISTS T_Tecnico(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR(75),
                email VARCHAR (50),
                especialidade VARCHAR (40)
              )
'''

scriptCriacao_tUsuario = '''
              CREATE TABLE IF NOT EXISTS T_Usuario(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR(50),
                email varchar(50),
                id_departamento INTEGER,
                FOREIGN KEY (id_departamento) REFERENCES T_Departamento(id)
              )
'''


scriptCriacao_tPrioridade =  '''
              CREATE TABLE IF NOT EXISTS T_Prioridade(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                descricao VARCHAR(20)
              )
'''

scriptCriacao_tAtivos =  '''
              CREATE TABLE IF NOT EXISTS T_Ativos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR(20),
                numero_serie VARCHAR(30),
                id_departamento INTEGER,
                FOREIGN KEY (id_departamento) REFERENCES T_Departamento(id)
              )
'''

scriptInsert_tChamado = {
  'script': '''
    INSERT INTO T_Chamado (descricao, 
                          data_Fechamento, 
                          data_abertura, 
                          status, 
                          id_Tecnico, 
                          id_Usuario, 
                          id_Prioridade,
                          id_Ativos)
    VALUES (?, ?, ?, ?, ?, ?, ?,?)
''',
'dado': dados.chamado }

scriptInsert_tDepartamento = {
    'script': '''
        INSERT INTO T_Departamento (descricao)
        VALUES (?)
    ''',
    'dado': dados.departamento
}

scriptInsert_tTecnico = {
  'script': '''
    INSERT INTO T_Tecnico (nome, email, especialidade)
    VALUES (?, ?, ?)
''',
'dado': dados.tecnico }

scriptInsert_tUsuario = {
  'script': '''
    INSERT INTO T_Usuario (nome, email, id_departamento)
    VALUES (?, ?, ?)
''',
'dado': dados.usuario }

scriptInsert_tPrioridade = {
  'script': '''
    INSERT INTO T_Prioridade (descricao)
    VALUES (?)
''',
'dado': dados.prioridade}

scriptInsert_tAtivos = {
  'script': '''
    INSERT INTO T_Ativos (nome, numero_serie, id_Departamento)
    VALUES (?,?,?)
''',
'dado': dados.ativos}


# Relação dos usuários em ordem crescente, com seus respectivos departamentos.
script_exercicio1 = f'''
                  SELECT * FROM T_Usuario u
                  inner join T_Departamento d
                  on u.id_departamento = d.id
                  ORDER BY u.nome               
'''

script_exercicio2 = f'''SELECT C.*, U.nome AS nome_usuario_abertura
FROM T_Chamado C
INNER JOIN T_Usuario U ON C.id_Usuario = U.id
'''
script_exercicio3 = f'''SELECT A.nome AS nome_ativo, D.descricao AS nome_departamento
FROM T_Ativos A
INNER JOIN T_Departamento D ON A.id_departamento = D.id;
'''
scriptsCriacao =  [scriptCriacao_tDepartamento,
                   scriptCriacao_tTecnico,
                   scriptCriacao_tPrioridade,
                   scriptCriacao_tUsuario,
                   scriptCriacao_tAtivos,
                   scriptCriacao_tChamado]


scriptsInserts = [scriptInsert_tDepartamento,
                 scriptInsert_tTecnico,
                 scriptInsert_tPrioridade,
                 scriptInsert_tUsuario,
                 scriptInsert_tAtivos,
                 scriptInsert_tChamado]
