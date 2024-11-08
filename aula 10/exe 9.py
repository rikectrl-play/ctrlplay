dias_totais = int(input())

anos = dias_totais // 365
resto = dias_totais % 365
meses = resto // 30
dias = resto % 30

print(f"{anos} Ano(s)")
print(f"{meses} meses(S)")
print(f"{dias} Dias(s)")