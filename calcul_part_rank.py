def calcular_nivel(vitorias, derrotas):
    saldo = vitorias - derrotas
    if vitorias < 10:
        nivel="Ferro"
    elif 11 <= vitorias <= 20:
        nivel="Bronze"
    elif 21 <= vitorias <= 50:
        nivel="Prata"
    elif 51 <= vitorias <= 80:
        nivel="Ouro"
    elif 81 <= vitorias <= 90:
        nivel="Diamante"
    elif 91 <= vitorias <= 100:
        nivel="Lendário"
    else:
        nivel="Imortal"

    return saldo, nivel
vitorias = int(input("Informe a quantidade de vitórias: "))
derrotas = int(input("Informe a quantidade de derrotas: "))

saldo_vitorias, nivel = calcular_nivel(vitorias, derrotas)
print(f"O herói tem saldo de {saldo_vitorias} e está no nível {nivel}")
