#matriz para armazenar os genêros de livros
nome_do_livro_genêro = [
#genêro literario de Terror
    ["O Exorcista", "It: A Coisa", "O Iluminado", "Mexican Gothic",
    "A Casa Infernal", "O Cemitério", "A Assombração da Casa da Colina",
    "Bird Box", "Drácula", "O Terror"], 
#genêro literario de Fantasia
    ["O Senhor dos Anéis", "As Crônicas de Nárnia", "O Nome do Vento",
    "A Guerra dos Tronos", "Mistborn: O Império Final", "O Ciclo da Herança",
    "A Terra das Sombras", "O Mago", "A Sombra do Vento", "O Hobbit"],
#genêro literario de Ação e Aventura
    ["Os Três Mosqueteiros", "O Código Da Vinci", "A Ilha do Tesouro",
    "O Último dos Moicanos", "O Conde de Monte Cristo", "A Conquista do Império",
    "Vingança","O Homem de Kiev","A Dança da Morte" ],
#genêro literario de Ficção Científica
    ["1984", "Fahrenheit 451", "Fundação", "Duna", "Neuromancer",
    "O Guia do Mochileiro das Galáxias", "O Homem do Castelo Alto",
    "A Máquina do Tempo", "Os Despossuídos", "Hyperion"],
#genêro literario de Humor
    ["O Guia do Mochileiro das Galáxias", "A Mãe","A Perda da Realidade",
    "Me Poupe!", "O Pequeno Príncipe", "Os Homens Explicam Tudo Para Mim",
    "Eu Sou Malala", "A Vida Intelectual", "O Mundo de Sofia", "Os Invisíveis"],
#genêro literario de Conto
    ["O Aleph", "Feliz Ano Novo", "Olhos D'Água", "O Coração Delator", "A Metamorfose",
    "O Conto da Ilha Desconhecida", "Doze Reis e a Moça Noiva", "A Morte de Ivan Ilitch",
    "Contos de Fadas", "O Grande Sertão: Veredas"],
#genêro literario de Thriller
    ["O Silêncio dos Inocentes", "A Garota no Trem", "Garota Exemplar", "Os Homens que Não Amavam as Mulheres",
    "O Colecionador de Ossos", "A Verdade Sobre o Caso Harry Quebert", "O Prisioneiro do Céu",
    "Antes Que Eu Vá", "O Enigma do Quatro", "A Mulher na Janela"],
#genêro literario de Romance
    ["Orgulho e Preconceito", "Como Eu Era Antes de Você", "A Culpa é das Estrelas", "O Morro dos Ventos Uivantes",
    "O Sol é Para Todos", "Noites de Tormenta", "Eleanor & Park", "O Duque e Eu", "A Biblioteca dos Mortos"],
] 

def interface():
    print("----------------------------------------------------------")

def usuario(usuario):
    
    if usuario == "S":
        usuario = (input("Informe o nome do usuário: "))
        print(usuario, "                                                 ")
    elif usuario == "N":
        print("Visitante", "                                                 ")

def usuario_livro(livros_consultados):
    livros_consultados = []
    if len(livros_consultados) == 0:
        print("Você não tem livros consultados!")
    else:
        print("Você tem", len(livros_consultados), "consultados")

def pesquisa(genêro):
    print()
    if genêro == "Terror":
        print(nome_do_livro_genêro[0])
    elif genêro == "Fantasia":
        print(nome_do_livro_genêro[1])
    elif genêro == "Ação/Aventura":
        print(nome_do_livro_genêro[2])
    elif genêro == "Ficção_Científica":
        print(nome_do_livro_genêro[3])
    elif genêro == "Humor":
        print(nome_do_livro_genêro[4])
    elif genêro == "Conto":
        print(nome_do_livro_genêro[5])
    elif genêro == "Thriller":
        print(nome_do_livro_genêro[6])
    elif genêro == "Romance":
        print(nome_do_livro_genêro[7])
    else:
        print("Por favor informe corretamente um tipo de genêro literario!")

def adicionar_livro(nome, genêro_do_livro, escritor):
    if genêro_do_livro == "Terror":
        nome_do_livro_genêro.append(nome[0])
    elif genêro_do_livro == "Fantasia":
        nome_do_livro_genêro.append(nome[1])
    elif genêro_do_livro == "Fantasia":
        nome_do_livro_genêro.append(nome[2])
    elif genêro_do_livro == "Fantasia":
        nome_do_livro_genêro.append(nome[3])
    elif genêro_do_livro == "Fantasia":
        nome_do_livro_genêro.append(nome[4])
    elif genêro_do_livro == "Fantasia":
        nome_do_livro_genêro.append(nome[5])
    elif genêro_do_livro == "Fantasia":
        nome_do_livro_genêro.append(nome[6])
    elif genêro_do_livro == "Fantasia":
        nome_do_livro_genêro.append(nome[7])
    else:
        print("Informe o genêro literario da obra!")
    
def remover_livro(nome, genêro_do_livro):
    print

def devolução_livro():
    print

interface()
print("                ", "Bem vindo a sua Biblioteca Virtual!", "               ")
usuario(input("Deseja fazer o login (S ou N)? "))
interface()
print("\n")
