def desvioPadraoDadosAgrupados(dados, media):
    soma = 0
    frequenciaTotal = 0
    for dado in dados:
        quadrado = ((dado["valorMedio"] - media) ** 2) * dado["frequencia"]
        soma += quadrado
        frequenciaTotal += dado["frequencia"]


    variancia = soma / frequenciaTotal
    print(variancia)
    return variancia ** (1/2)


def mediaDadosAgrupados(dados):
    soma = 0
    frequenciaTotal = 0
    for dado in dados:
        soma += dado["valorMedio"] * dado["frequencia"]
        frequenciaTotal += dado["frequencia"]

    return soma/frequenciaTotal


if __name__ == "__main__":
    dados = [
        {
            "valorMedio": 1,
            "frequencia": 23
        },
        {
            "valorMedio": 4,
            "frequencia": 33
        },
        {
            "valorMedio": 7,
            "frequencia": 63
        },
        {
            "valorMedio": 10,
            "frequencia": 68
        },
        {
            "valorMedio": 13,
            "frequencia": 19
        },
        {
            "valorMedio": 16,
            "frequencia": 10
        },
        {
            "valorMedio": 19,
            "frequencia": 1
        },

        {
            "valorMedio": 22,
            "frequencia": 0
        },
    ]

    print(mediaDadosAgrupados(dados))
    print(desvioPadraoDadosAgrupados(dados, mediaDadosAgrupados(dados)))