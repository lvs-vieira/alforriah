# Exercício proposto
# Criar uma base de dados fictícia no formato CSV. 
# Por exemplo, você poderia fazer um programa em Python para escrever um arquivo CSV que tivesse:
# 1. Nome
# 2. Data de nascimento
# 3. Estado (UF)
# 4. Peso
# 5. Altura

import os # This module provides a portable way of using operating system dependent functionality.

def solicitar_dados():
    nome        = input('Nome: ')
    data_nasc   = input('Data de nascimento: ')
    uf          = input('Estado: ')
    peso        = input('Peso: ')
    altura      = input('Altura: (exemplo: 1.79 ')
    dados       = (nome,data_nasc,uf,peso,altura)
    return dados      

def solicitar_dados_busca():
    #print('Digite o nome que deseja procurar \n')
    nome        = input('Digite o NOME que deseja procurar: ')
    data_nasc   = input('Digite a DATA DE NASCIMENTO: ')
    dados       = (nome,data_nasc)
    return dados      

def criar_base_dados(caminho):
    colunas = ['nome', 'data_nasc', 'uf', 'peso', 'altura']
    arquivo = open(caminho,'w')
    linha = ','.join(colunas)
    arquivo.write(linha + '\n')
    arquivo.close()
    print("Base de dados criada com sucesso!")

def cadastrar(dados,caminho):
    arquivo = open(caminho,'a')
    arquivo.write(','.join(dados) + '\n')
    arquivo.close()
    print("Cadastro efetuado com sucesso!")

def localizar_cadastro(dados, caminho):
    arquivo = open(caminho)
    linhas = arquivo.readlines()
    arquivo.close()
    for linha in linhas:
        dados_cadastro = linha.strip().split(',') # strip remove espaços em branco, inicio e fim
        if dados[0] == dados_cadastro[0] and dados[1] == dados_cadastro[1]: # ver criar indices para facilitar a leitura 
            return dados_cadastro
    return []

caminho = 'base_dados.csv'
if not os.path.exists(caminho):
    criar_base_dados('base_dados.csv')

#dados_cadastro = solicitar_dados()
#cadastrar(dados_cadastro,'base_dados.csv') 

# Solicitar dados para busca
dados = solicitar_dados_busca()
dados_cadastro = localizar_cadastro(dados,caminho)

if dados_cadastro:
    print(f'O nome procurado: {dados[0]} esta cadastrado na base de dados.')
else:
    print(f'O nome procurado: {dados[0]} NÃO esta cadastrado na base de dados.')