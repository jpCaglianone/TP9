from datetime import date

usuario = [
    ["Nome","Email","Id_Departamento"],
    ["Felipe Guimarães","fguimaraes@healthtech.com",6],
    ["Lucas Pereira","fguimaraes@healthtech.com",2],
    ["Maria Silva","fguimaraes@healthtech.com",4],
    ["João Santos","fguimaraes@healthtech.com",1],
    ["Gabriela Oliveira","fguimaraes@healthtech.com",2],
    ["Matheus Rodrigues","fguimaraes@healthtech.com",1],
    ["Ana Souza","fguimaraes@healthtech.com",3],
    ["Rafael Costa","fguimaraes@healthtech.com",6],
    ["Isabela Almeida","fguimaraes@healthtech.com",2],
    ["Pedro Ferreira","fguimaraes@healthtech.com",5],
    ["Fernanda Lima","fguimaraes@healthtech.com",3],
    ["Larissa Gonçalves","fguimaraes@healthtech.com",1],
    ["Guilherme Carvalho","fguimaraes@healthtech.com",6],
    ["Vitória Ribeiro","fguimaraes@healthtech.com",5],
    ["Thiago Miranda","fguimaraes@healthtech.com",6],
    ["Juliana Castro","fguimaraes@healthtech.com",3],
    ["Diego Santos","fguimaraes@healthtech.com",4],
    ["Bianca Martins","fguimaraes@healthtech.com",2],
    ["Felipe Gomes","fguimaraes@healthtech.com",4],
    ["Camila Moreira","fguimaraes@healthtech.com",6]
]

departamento = [
    ["Descrição"],
    ["Financeiro/Contabilidade"],
    ["Área Técnica"],
    ["Administração"],
    ["Recursos Humanos"],
    ["Marketing"],
    ["Operações"]
]

chamado = [
    ["Descrição", "Id_Prioridade", "Status", "Data_abertura", "Data_Fechamento", "Id_Tecnico","Id_Usuario"],
    ["Troca do mouse", "2", "Aberto" ,date(2023,6,11), 0, 4, 1],
    ["Recarga tinta impressora", "3", "Fechado" ,date(2022,2,14), date(2022,3,1), 4, 1],
    ["Habilitação site pesquisa", "3", "Aberto" ,date(2023,6,11), 0, 2, 8],
    ["Queda de rede, reconfiguração de switchs", "1", "Aberto" ,date(2023,6,11), 0, 2, 6],
    ["Sem internet", "1", "Aberto" ,date(2023,6,11), 0, 2, 1],
    ["Mal contato cabo de rede", "2", "Aberto" ,date(2023,6,11), 0, 4, 5],
    ["Equipamento não liga, cheiro de queimado", "1", "Aberto" ,date(2023,6,11), 0, 4, 7],
    ["Mal contato no cabo de video", "2", "Aberto" ,date(2023,6,11), 0, 4, 8],
    ["Atolamento de papel na impressora", "3", "Aberto" ,date(2023,6,11), 0, 4, 10],
    ["IP com conflito geral", "1", "Aberto" ,date(2023,6,11), 0, 5, 1],
    ["Teclado com teclas defeituosas, precisando de troca", "2", "Aberto" ,date(2023,6,11), 0, 4, 6],
    ["Botão de ligar o computador com mal contato", "3", "Aberto" ,date(2023,6,11), 0, 5, 3],
    ["Instalação de software homologado", "2", "Aberto" ,date(2023,6,11), 0,1, 16],
    ["Computador com virus", "1", "Aberto" ,date(2023,6,11), 0,3, 15],
    ["Erro compatibilidade de software", "2", "Aberto" ,date(2023,6,11), 0,1, 11]
]

tecnico = [
    ["Nome", "Email", "Especialidade"],
    ["Joào Xavier", "jxavieir@healthtech.com", "Softwares"],
    ["Ana Coutinho", "acoutinho@healthtech.com", "Redes e segurança"],
    ["Fabiola Pinheiro", "fpinheiro@healthtech.com", "Segurança"],
    ["Gustavo Cardoso", "gcardoso@healthtech.com", "Hardware e periféricos"],
    ["Alex Bertolatti", "abertolatti@healthtech.com", "Servidores e banco de dados"]
]

prioridade =[
    ["Prioridade"],
    ["Alta"],
    ["Média"],
    ["Baixa"]
]
