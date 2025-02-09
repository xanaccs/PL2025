import re 
import sys

# Definição das expressões regulares pertinentes
inteiro = r'[+\-]?\d+'
on = r'[Oo][Nn]'
off = r'[Oo][Ff]{2}'
equal = r'='

# Variável que irá armazenar o estado da soma
soma = 0
ativo = True




                
if __name__ == "__main__":
    somador("exemplo.txt")