# [TPC4] Analisador Léxico 

## 👤 Autor  
 - **Nome**: Alexandra Costa Coelho dos Santos
 - **Número**: A94523

## 📜 Descrição
O ficheiro tpc4.py contém um **lexer** que processa consultas SPARQL e divide os componentes da linguagem em tokens. O código identifica elementos como palavras-chave (SELECT, WHERE, LIMIT), variáveis (?nome, ?desc), strings, números, prefixos e predicados.


## 📂 Estrutura dos Tokens
Os tokens identificados no código são:
- COMMENT → Comentários iniciados por #
- SELECT, WHERE, LIMIT → Palavras-chave da linguagem
- VAR → Variáveis iniciadas por ?
- STRING → Sequências entre aspas "..."
- NUMERO → Números inteiros
- PREFIXO → Prefixos terminados em .
- PREDICADO → Identificadores genéricos
- ACHAVE, FCHAVE → { e }
- PONTO → . (ponto final de uma instrução)

## 🚀 Como Executar
1. **Executar o analisador**
   
bash
   python3 tpc4.py


O código lê a consulta SPARQL e imprime os tokens reconhecidos.
