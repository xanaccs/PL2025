import sys

def on_off(texto):

    soma = 0
    ligado = True  
    resultado = []
    
    palavras = texto.split()

    for palavra in palavras:
        if palavra.lower() == 'off':
            ligado = False
            resultado.append("OfF")
        elif palavra.lower() == 'on':
            ligado = True
            resultado.append("ON")
        elif palavra == "=":
            resultado.append(f">> {soma}")  
        elif ligado:  
            if palavra.isdigit():
                soma += int(palavra)
    
    resultado.append(f">> {soma}")
    
    return "\n".join(resultado)

if __name__ == "__main__":
    with open('exemplo.txt', 'r') as f:
        texto_entrada = f.read()
    print(texto_entrada)
    print(on_off(texto_entrada))
