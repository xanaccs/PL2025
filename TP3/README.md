# [TPC4] Conversor de Markdown para HTML

## 👤 Autor  
 - **Nome**: Alexandra Costa Coelho dos Santos
 - **Número**: A94523

## 📜 Descrição
O tpc3 implementa um conversor de arquivos **Markdown** para **HTML** utilizando Python. O script lê um arquivo Markdown, converte seus elementos para HTML e guarda o resultado num arquivo de saída.

## ⚙️ Funcionalidades
O conversor suporta os seguintes elementos do Markdown:

- **Cabeçalhos**: Converte `#`, `##`, `###` em `<h1>`, `<h2>`, `<h3>`.
- **Texto Negrito**: Converte o texto entre `**` em `<b>`.
- **Texto Itálico**: Converte o texto entre `*` em `<i>`.
- **Listas Numeradas**: Converte listas numeradas em uma lista ordenada HTML (`<ol><li>...</li></ol>`).
- **Links**: Converte links de Markdown (`[texto](URL)`) para `<a href="URL">texto</a>`.
- **Imagens**: Converte imagens de Markdown (`![alt text](URL)`) para a tag HTML `<img src="URL" alt="alt text"/>`.

## 🛠️ Como Funciona

1. O script lê um arquivo Markdown fornecido como argumento ou usa um arquivo padrão chamado `exemplo.md`.
2. Utilizando as expressões regulares, o conteúdo do arquivo Markdown é processado e convertido para HTML.
3. O resultado da conversão é gravado em um arquivo de saída (`resultado.html`).

## 🚀 Como Executar

1. Execução com os parâmetros padrão (arquivo de entrada `exemplo.md` e saída `resultado.html`):

    ```bash
    python3 tpc3.py
    ```

2. Caso o arquivo de entrada não seja encontrado ou haja outro erro, o script exibirá uma mensagem de erro.
