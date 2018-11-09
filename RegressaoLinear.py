#TRABALHO DE TÓPICOS AVANÇADOS DE BANCO DE DADOS
#ALUNOS: LEONARDO MARCO | MARIA CLARA | MARIANE LUIZA
#PROF: FELIPE LEANDRO
#CURSO: CIÊNCIA DA COMPUTAÇÃO

import csv
import numpy as np
import matplotlib.pyplot as plt


preço_barroca = []
vagas_barroca = []
areaUtil_barroca = []
iptu_barroca = []
preço_total = []
areaUtil_total = []

f = csv.reader(open('imobiliaria.csv'), delimiter=';')
for [imovel_Id,tipoImovel,valorImovel,areaRealPrivativa,latitude,longitude,quartos,banho,suites,vagaGaragem,valorCondominio,valorIptu,Cidade,Regiao,Bairro,Endereco] in f:
    if valorImovel != 'valorImovel' and Bairro == 'Alto Barroca':
        preço_barroca.append(int(valorImovel))
    if vagaGaragem != 'vagaGaragem' and Bairro == 'Alto Barroca':
        vagas_barroca.append(int(vagaGaragem))
    if quartos != 'quartos' and Bairro == 'Alto Barroca':
        areaUtil_barroca.append(int(quartos+banho+suites))
    if valorIptu != 'valorIptu' and Bairro == 'Alto Barroca':
        valorIptu = valorIptu.replace(',', '.')
        iptu_barroca.append(float(valorIptu))
    if valorImovel != 'valorImovel':
        preço_total.append(int(valorImovel))
    if quartos != 'quartos':
        areaUtil_total.append(int(quartos + banho + suites))


def grafico_rl(a,b,c,d,questao):
    x = np.array(a)
    y = np.array(b)
    p1 = np.polyfit(x, y, 1)
    yfit = p1[0] * x + p1[1]
    yresid = y - yfit
    SQresid = sum(pow(yresid, 2))
    SQtotal = len(y) * np.var(y)
    R2 = 1 - SQresid / SQtotal


    plt.plot(x, y, 'o')
    plt.plot(x, np.polyval(p1, x), 'g--')
    plt.xlabel(c)
    plt.ylabel(d)
    plt.show()

    PrimeirPa = a
    SegundPa = b
    m = sum(Pa * Pb for (Pa, Pb) in zip(PrimeirPa, SegundPa)) - sum(PrimeirPa) * sum(SegundPa) / len(PrimeirPa)
    m /= sum(Pa ** 2 for Pa in PrimeirPa) - (sum(PrimeirPa) ** 2) / len(PrimeirPa)
    Pb = sum(SegundPa) / len(SegundPa) - m * sum(PrimeirPa) / len(PrimeirPa)
    print('Resultado ideal da '+questao+' questão')
    print(m * 5 + Pb)
    print('\n')

grafico_rl(preço_barroca, vagas_barroca, "Preço", "Vagas", "primeira")
grafico_rl(preço_barroca, areaUtil_barroca, "Preço", "Area util", "segunda")
grafico_rl(preço_barroca, iptu_barroca, "Preço", "Valor IPTU", "terceira")
grafico_rl(preço_total, areaUtil_total, "Preço de todos os imoveis", "Vagas de todos os imoveiss", "quarta")