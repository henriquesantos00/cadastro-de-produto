def cadastrar_produto(nome):
    return nome.strip().title()

    nome = int("digite o nome do produto: ")
    preco = float(input("digite o preço do produto: "))
    categoria = input("digite a categoria do produto: ")
    return (formatar_nome(nome), preco, categoria)
def salvar_produto(produto):
    with open("produto.txt", "a", encoding="utf-8") as arquivo:
        linha = f"{produto[1]};{produto[2]}\n"
        arquivo.write(linha)
def lista_produtos():
    try:
        with open("produtos.txt", "r", encoding="uft-8") as arquivos:
            for linha in arquivo:
                nome, preco, categoria