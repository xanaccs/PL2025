import re

def ler_dataset(file_name):
    with open(file_name, "r", encoding="utf-8-sig") as f:
        linhas = f.read()
    
    # Expressão regular para dividir linhas, ignorando newlines dentro de aspas
    padrao_linhas = r'\n(?=(?:[^"]*"[^"]*")*[^"]*$)'
    linhas = re.split(padrao_linhas, linhas)
    
    dados = []
    
    # Expressão regular para dividir corretamente
    padrao = r';(?=(?:[^"]*"[^"]*")*[^"]*$)'
    
    for linha in linhas[1:]:
        if linha.strip():  # Evita processar linhas vazias
            campos = re.split(padrao, linha)
            campos = [campo.strip('"') for campo in campos]
            
            if len(campos) >= 5:  # Garante que há campos suficientes
                nome, _, _, periodo, compositor = campos[:5]  # Considera apenas os primeiros 5 campos
                dados.append((nome, periodo, compositor))
    
    return dados

def processar_dados(dados):
    compositores = set()
    distPeriodo = {}
    obrasPeriodo = {}
    
    for nome, periodo, compositor in dados:
        compositores.add(compositor)
        
        if periodo not in distPeriodo:
            distPeriodo[periodo] = 0
            obrasPeriodo[periodo] = []
        
        distPeriodo[periodo] += 1
        obrasPeriodo[periodo].append(nome)
    
    return sorted(compositores), distPeriodo, {period: sorted(obras) for period, obras in obrasPeriodo.items()}

def escrever_resultados(compositores, distPeriodo, obrasPeriodo):
    print("A escrever para output.txt..")

    with open("output.txt", "w", encoding="utf-8") as f:
        f.write("Lista ordenada de compositores:\n")
        f.write("\n".join(compositores) + "\n\n")
        
        f.write("Distribuição das obras por período:\n")
        for periodo, nobras in distPeriodo.items():
            f.write(periodo + ":" + str(nobras) + "\n")
        f.write("\n")
        
        f.write("Obras por período:\n")
        for periodo, obras in obrasPeriodo.items():
            f.write(periodo + ": " + "\n".join(obras) + "\n")
        
    print("Ficheiro output.txt criado!")


def main():
    file_name = "obras.csv"
    dados = ler_dataset(file_name)
    compositores, distPeriodo, obrasPeriodo = processar_dados(dados)
    escrever_resultados(compositores, distPeriodo, obrasPeriodo)

if __name__ == "__main__":
    main()
