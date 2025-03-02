# [TPC3] Conversor de MarkDown para HTML

# Conversor Markdown para HTML

Este é um conversor simples de Markdown para HTML, desenvolvido em Python. O script converte os principais elementos da **Basic Syntax** do Markdown (como cabeçalhos, negrito, itálico, listas numeradas, links e imagens) para HTML.

## Funcionalidades

O conversor suporta os seguintes elementos do Markdown:

- **Cabeçalhos**:
  - `# Título` → `<h1>Título</h1>`
  - `## Subtítulo` → `<h2>Subtítulo</h2>`
  - `### Subsubtítulo` → `<h3>Subsubtítulo</h3>`

- **Texto em Negrito**:
  - `**texto**` → `<b>texto</b>`

- **Texto em Itálico**:
  - `*texto*` → `<i>texto</i>`

- **Listas Numeradas**:
  - `1. item` → `<ol><li>item</li></ol>`

- **Links**:
  - `[texto](URL)` → `<a href="URL">texto</a>`

- **Imagens**:
  - `![texto alternativo](URL)` → `<img src="URL" alt="texto alternativo"/>`

## Como Usar

1. No terminal, execute o script passando o caminho para o arquivo Markdown como argumento:
   ```bash
   python3 tpc3.py exemplo.md
2. O script vai imprimir o conteúdo do arquivo Markdown que foi convertido para HTML, no terminal.
