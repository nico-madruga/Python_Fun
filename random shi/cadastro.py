class Aluno:

    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf


        
def cadastrarAluno(nome, idade, cpf):
    aluno = Aluno(nome, idade, cpf)
    return aluno

alunos = []
sistemaRodando = True

while sistemaRodando:

    print("""
    =====MENU=====
    1 - Cadastrar Aluno
    2 - Listar Alunos
    3 - Mostrar média das idades
    4 - Sair
    """)

    escolha = float(input("Insira o numero da ação que você deseja realizar: "))

    match escolha:
        case 1:
            nome = input("Insira o nome do Aluno: ")
            idade = float(input("Insira a idade do Aluno: "))
            cpf = input("Insira o CPF do Aluno: ")

            aluno = cadastrarAluno(nome, idade, cpf)
            alunos.append(aluno)

        case 2:
            for aluno in alunos:
                print("Nome:", aluno.nome,
                      "\nIdade:", aluno.idade,
                      "\nCPF:", aluno.cpf)
        case 3:
            totalIdades = len(alunos)
            somaIdade = 0

            for aluno in alunos:
                somaIdade += aluno.idade

            mediaIdade = somaIdade/totalIdades
            print("A média das idades dos alunos é", mediaIdade)
        case _:
            sistemaRodando = False