import re
import sys

def markdown_to_html(texto):

    # Cabeçalhos
    texto = re.sub(r'^### (.*)', r'<h3>\1</h3>', texto, flags=re.MULTILINE)
    texto = re.sub(r'^## (.*)', r'<h2>\1</h2>', texto, flags=re.MULTILINE)
    texto = re.sub(r'^# (.*)', r'<h1>\1</h1>', texto, flags=re.MULTILINE)
    
    # Texto a Negrito
    texto = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', texto)
    
    # Texto em Itálico
    texto = re.sub(r'\*(.*?)\*', r'<i>\1</i>', texto)
    
    # Listas Numeradas
    texto = re.sub(r'\n\d+\. (.*)', r'\n<li>\1</li>', texto)
    texto = re.sub(r'(<li>.*</li>)', r'<ol>\n\1\n</ol>', texto, flags=re.DOTALL)
    
    # Links
    texto = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', texto)
    
    # Imagens
    texto = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1"/>', texto)
    
    return texto

def main(file="exemplo.md"):
    try:
        with open(file, "r", encoding="utf-8") as f:
            markdown = f.read()
        
        html = markdown_to_html(markdown)
        print(html)
    except FileNotFoundError:
        print(f"Erro: O arquivo '{file}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    file = sys.argv[1] if len(sys.argv) > 1 else "exemplo.md"
    main(file)