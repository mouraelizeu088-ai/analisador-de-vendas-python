import csv

print("=" * 55)
print("          ANALISADOR DE VENDAS")
print("=" * 55)

faturamento_total = 0
custo_total = 0
lucro_total = 0
quantidade_total = 0

produto_mais_vendido = ""
maior_quantidade = 0

produto_mais_lucrativo = ""
maior_lucro = 0

vendas_validas = 0
erros = []

try:
    with open("vendas.csv", "r", encoding="utf-8") as arquivo:
        vendas = csv.DictReader(arquivo)

        print("\n--- ANÁLISE POR PRODUTO ---\n")

        for numero_linha, venda in enumerate(vendas, start=2):
            try:
                produto = venda["produto"].strip()

                if not produto:
                    raise ValueError("Nome do produto vazio")

                quantidade = int(venda["quantidade"])
                preco = float(venda["preco_venda"])
                custo = float(venda["custo_unitario"])

                if quantidade <= 0:
                    raise ValueError("Quantidade deve ser maior que zero")

                if preco < 0 or custo < 0:
                    raise ValueError("Preço e custo não podem ser negativos")

                faturamento = quantidade * preco
                custo_produto = quantidade * custo
                lucro = faturamento - custo_produto

                faturamento_total += faturamento
                custo_total += custo_produto
                lucro_total += lucro
                quantidade_total += quantidade
                vendas_validas += 1

                if quantidade > maior_quantidade:
                    maior_quantidade = quantidade
                    produto_mais_vendido = produto

                if lucro > maior_lucro:
                    maior_lucro = lucro
                    produto_mais_lucrativo = produto

                print(
                    f"{produto} | "
                    f"Qtd: {quantidade} | "
                    f"Faturamento: R$ {faturamento:.2f} | "
                    f"Lucro: R$ {lucro:.2f}"
                )

            except (ValueError, TypeError, KeyError) as erro:
                erros.append(f"Linha {numero_linha}: {erro}")

except FileNotFoundError:
    print("\nERRO: O arquivo vendas.csv não foi encontrado.")
    print("Coloque vendas.csv na mesma pasta do programa.")
    exit()

if vendas_validas == 0:
    print("\nNenhuma venda válida foi encontrada.")
    exit()

margem_total = (lucro_total / faturamento_total) * 100 if faturamento_total else 0

print("\n" + "=" * 55)
print("RESUMO GERAL")
print("=" * 55)

print(f"Registros válidos: {vendas_validas}")
print(f"Unidades vendidas: {quantidade_total}")
print(f"Faturamento total: R$ {faturamento_total:.2f}")
print(f"Custo total: R$ {custo_total:.2f}")
print(f"Lucro bruto total: R$ {lucro_total:.2f}")
print(f"Margem de lucro: {margem_total:.2f}%")

print("\n--- DESTAQUES ---")
print(f"Produto mais vendido: {produto_mais_vendido} ({maior_quantidade} unidades)")
print(f"Produto mais lucrativo: {produto_mais_lucrativo} (R$ {maior_lucro:.2f})")

print("\n--- VALIDAÇÃO DOS DADOS ---")

if erros:
    print(f"Foram encontrados {len(erros)} problema(s):")
    for erro in erros:
        print("-", erro)
else:
    print("Nenhum erro encontrado nos dados.")

print("\nAnálise concluída com sucesso.")

with open("relatorio_vendas.txt", "w", encoding="utf-8") as relatorio:
    relatorio.write("RELATÓRIO DE VENDAS\n")
    relatorio.write("=" * 40 + "\n\n")

    relatorio.write(f"Registros válidos: {vendas_validas}\n")
    relatorio.write(f"Unidades vendidas: {quantidade_total}\n")
    relatorio.write(f"Faturamento total: R$ {faturamento_total:.2f}\n")
    relatorio.write(f"Custo total: R$ {custo_total:.2f}\n")
    relatorio.write(f"Lucro bruto total: R$ {lucro_total:.2f}\n")
    relatorio.write(f"Margem de lucro: {margem_total:.2f}%\n\n")

    relatorio.write("DESTAQUES\n")
    relatorio.write("-" * 40 + "\n")
    relatorio.write(
        f"Produto mais vendido: {produto_mais_vendido} "
        f"({maior_quantidade} unidades)\n"
    )
    relatorio.write(
        f"Produto mais lucrativo: {produto_mais_lucrativo} "
        f"(R$ {maior_lucro:.2f})\n"
    )

    relatorio.write("\nVALIDAÇÃO DOS DADOS\n")
    relatorio.write("-" * 40 + "\n")

    if erros:
        for erro in erros:
            relatorio.write(f"- {erro}\n")
    else:
        relatorio.write("Nenhum erro encontrado nos dados.\n")

print("Relatório criado: relatorio_vendas.txt")
