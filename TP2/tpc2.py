def ler_ficheiro(idade, modalidade, resultado):
    ficheiro = open("emd.csv")
    ficheiro.readline() 
    for linha in ficheiro:
        campos = linha.split(",")
        idade.append(int(campos[5]))
        modalidade.append(campos[8])
        resultado.append(campos[12].rstrip())  # retirar a new line
    ficheiro.close()

def modalidades_ordenadas(modalidade):
    ordenado = sorted(set(modalidade))
    print("\n----- Aqui estão as modalidades ordenadas: -----\n")
    for mod in ordenado:
        print(f"- {mod}")