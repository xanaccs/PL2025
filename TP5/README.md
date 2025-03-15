# [TPC5] Máquina de Vendas 

## 👤 Autor  
 - **Nome**: Alexandra Costa Coelho dos Santos
 - **Número**: A94523

## 📜 Descrição
O ficheiro `tpc5.py` implementa uma **máquina de vendas** que simula o processo de compra de produtos. A máquina permite listar os produtos disponíveis no stock, adicionar moedas, selecionar produtos para comprar, adicionar novos produtos e devolver troco. O código também mantém o controle do stock de produtos, armazenando e atualizando os dados em um ficheiro JSON.

## 📂 Funcionalidades
- **LISTAR** → Exibe todos os produtos disponíveis no stock.
- **MOEDA [valor]** → Adiciona moedas ao saldo, com valores em euros (e) e centimos (c).
- **SELECIONAR [código]** → Permite ao utilizador selecionar um produto para comprar, verificando o saldo e a disponibilidade.
- **ADICIONAR** → Adiciona um novo produto ao stock.
- **SAIR** → Finaliza a interação, devolvendo o troco, se houver troco (saldo que restou).

## 🚀 Como Executar
1. **Preparar o arquivo de estoque**
   Criar o arquivo `stock.json` com os produtos disponíveis. Exemplo de estrutura de dados:

```json
{
   "stock": [
    {
        "cod": "A1",
        "nome": "Cola",
        "quant": 10,
        "preco": 1.0
    },
    {
        "cod": "A2",
        "nome": "Fanta",
        "quant": 8,
        "preco": 1.0
    }
  ]
}

````
**Executar o script**  
   Após preparar o arquivo de estoque, execute o script com o seguinte comando:

```bash
python3 tpc5.py
```

2. **Interagir com a máquina**  
   Após a execução, você pode interagir com a máquina utilizando os seguintes comandos:

   - **LISTAR**: Lista os produtos disponíveis no stock.
   - **MOEDA [valor]**: Adiciona moedas ao saldo (exemplo: `MOEDA 1e`, `MOEDA 50c`).
   - **SELECIONAR [código]**: Seleciona um produto para compra (exemplo: `SELECIONAR A1`).
   - **ADICIONAR**: Adiciona um novo produto ao stock.
   - **SAIR**: Finaliza a interação e devolve o troco, se houver.

## 📂 Estrutura do Código
- **Função `carregar_stock(ficheiro)`**: Carrega o stock a partir de um arquivo JSON.
- **Função `listar_produtos(stock)`**: Exibe os produtos disponíveis no stock.
- **Função `adicionar_moeda(moedas, saldo)`**: Adiciona moedas ao saldo da máquina.
- **Função `selecionar(stock, cod, saldo)`**: Permite selecionar um produto para compra.
- **Função `adicionar_produto(stock)`**: Adiciona um novo produto ao stock.
- **Função `sair(saldo)`**: Finaliza a interação e devolve o troco.




