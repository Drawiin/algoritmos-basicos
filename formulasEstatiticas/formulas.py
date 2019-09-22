def desvioPadraoDadosAgrupados(dados, media):
    soma = 0
    frequenciaTotal = 0
    for dado in dados:
        quadrado = ((dado["valorMedio"] - media) ** 2) * dado["frequencia"]
        soma += quadrado
        frequenciaTotal += dado["frequencia"]


    variancia = soma / frequenciaTotal
    print('variancia',variancia)
    return variancia ** (1/2)


def mediaDadosAgrupados(dados):
    soma = 0
    frequenciaTotal = 0
    for dado in dados:
        soma += dado["valorMedio"] * dado["frequencia"]
        frequenciaTotal += dado["frequencia"]

    print('Frequencia Toltal', frequenciaTotal)
    return soma/frequenciaTotal

def calculaMediana(limiteInferior, posicaoMediana, frequeAcuClasAnterior, larguraIntervalorClasse, frequeClasMediana):
    return limiteInferior+(posicaoMediana-frequeAcuClasAnterior)*(larguraIntervalorClasse/frequeClasMediana)



if __name__ == "__main__":
    dados = [
        {
            "valorMedio": 1,
            "frequencia": 35
        },
        {
            "valorMedio": 4,
            "frequencia": 57
        },
        {
            "valorMedio": 7,
            "frequencia": 41
        },
        {
            "valorMedio": 10,
            "frequencia": 10
        },
        {
            "valorMedio": 13,
            "frequencia": 8
        },
        {
            "valorMedio": 16,
            "frequencia": 0
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

    print('media',mediaDadosAgrupados(dados))
    print('desvio padrão',desvioPadraoDadosAgrupados(dados, mediaDadosAgrupados(dados)))
    print('mediana', calculaMediana(9, 163, 119, 3, 10))