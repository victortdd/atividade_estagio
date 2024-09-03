import json

with open('dados.json', 'r') as file:
    data = json.load(file)

faturamento_diario = list(data.values())
faturamento_valido = [valor for valor in faturamento_diario if valor > 0]

menor_faturamento = min(faturamento_valido)
maior_faturamento = max(faturamento_valido)

media_mensal = sum(faturamento_valido) / len(faturamento_valido)
dias_acima_da_media = sum(1 for valor in faturamento_valido if valor > media_mensal)

print(f"Menor faturamento: R${menor_faturamento:.2f}")
print(f"Maior faturamento: R${maior_faturamento:.2f}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media} dias")
