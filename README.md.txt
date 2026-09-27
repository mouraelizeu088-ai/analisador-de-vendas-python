# Analisador de Vendas em Python

Projeto desenvolvido para praticar programação em Python, manipulação de arquivos CSV, validação de dados e geração automática de relatórios.

## Funcionalidades

O programa:

- Lê dados de vendas a partir de um arquivo CSV.
- Calcula faturamento, custos e lucro bruto por produto.
- Calcula faturamento, custo, lucro e margem total.
- Identifica o produto mais vendido.
- Identifica o produto mais lucrativo.
- Valida registros e identifica dados inválidos.
- Continua a análise mesmo quando encontra um registro incorreto.
- Gera automaticamente um relatório em arquivo TXT.

## Estrutura do projeto

- `analisador.py` - código principal.
- `vendas.csv` - dados utilizados na análise.
- `relatorio_vendas.txt` - relatório gerado automaticamente.
- `README.md` - documentação do projeto.

## Como executar

Abra o terminal na pasta do projeto e execute:

py analisador.py

O programa analisará o arquivo `vendas.csv`, exibirá os resultados no terminal e criará automaticamente o arquivo `relatorio_vendas.txt`.

## Validação de dados

O programa possui tratamento de erros para registros inválidos.

Por exemplo, se uma quantidade que deveria ser numérica possuir um texto, o registro é identificado como inválido e os demais dados continuam sendo processados normalmente.

## Tecnologias utilizadas

- Python
- CSV
- Manipulação de arquivos
- Tratamento de exceções

## Objetivo

Este projeto foi desenvolvido como projeto de aprendizado e prática de programação em Python, com foco em análise de dados, automação de cálculos e tratamento de erros.
