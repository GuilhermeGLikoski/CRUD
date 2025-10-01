import re
import os 

def cadastro_novo_usuario():
    while True:
        erros = []
        nome = None
        email = None
        senha = None

        nome_digitado = input("Digite apenas seu primeiro nome: ").strip()
        if nome_digitado.isalpha():
            if len(nome_digitado) >= 3:
                nome = nome_digitado
            else:
                erros.append("Nome deve ter no mínimo 3 digitos.")
        else:
            erros.append("Nome deve ter apenas letras")

        email_digitado = input("Digite um novo email: ").strip().lower()
        if re.match(r"[^@]+@(gmail\.com|yahoo\.com|outlook\.com|hotmail\.com)$", email_digitado):
            email = email_digitado
        erros.append("Digite o email com algum domínio existente.")

        senha_digitada = input("Digite uma senha: ")
