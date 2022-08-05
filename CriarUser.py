from ast import Pass
from json import load
import os

#Tornar grupo dono de diretório... Perguntar se apenas o grupo deve ter acesso ao diretorio. 770 - Dono e Grupo podem tudo e outros nada... 777 Geral pode tudo...

def start():
    print("1 - Criar diretório de grupo ?\n"
     "2 - Criar grupo ?\n"
      "3 - Criar usuário ?\n"
       "4 - Tornar grupo, já existente, dono de um diretório ?\n"
        "5 - Tornar diretório publico ?")
    EscolhaMenu = input("O que vamos fazer ?")

if __name__ == '__main__':
    start()