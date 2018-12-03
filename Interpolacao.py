#TRABALHO DE TÓPICOS AVANÇADOS DE BANCO DE DADOS - 2
#ALUNOS: LEONARDO MARCO | MARIA CLARA | MARIANE LUIZA | SAMUEL PEREIRA
#PROF: FELIPE LEANDRO
#CURSO: CIÊNCIA DA COMPUTAÇÃO

from pylab import *
import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

preço_barroca = []
vagas_barroca = []
areaUtil_barroca = []
iptu_barroca = []
preço_total = []
areaUtil_total = []

f = csv.reader(open('imobiliaria.csv'), delimiter=';')
for [imovel_Id, tipoImovel, valorImovel, areaRealPrivativa, latitude, longitude, quartos, banho, suites, vagaGaragem,
     valorCondominio, valorIptu, Cidade, Regiao, Bairro, Endereco] in f:
    if valorImovel != 'valorImovel' and Bairro == 'Alto Barroca':
        preço_barroca.append(int(valorImovel))
    if vagaGaragem != 'vagaGaragem' and Bairro == 'Alto Barroca':
        vagas_barroca.append(int(vagaGaragem))
    if quartos != 'quartos' and Bairro == 'Alto Barroca':
        areaUtil_barroca.append(int(quartos + banho + suites))
    if valorIptu != 'valorIptu' and Bairro == 'Alto Barroca':
        valorIptu = valorIptu.replace(',', '.')
        iptu_barroca.append(float(valorIptu))
    if valorImovel != 'valorImovel':
        preço_total.append(int(valorImovel))
    if quartos != 'quartos':
        areaUtil_total.append(int(quartos + banho + suites))


def grafico_lagrange(x, y, z, desc1):
    count = 0
    quantidade = []
    for val in x:
        count += 1
        quantidade.append(count)


    interpolado = interpolate.interp1d(quantidade, y)
    plt.plot(np.linspace(1, count, count), interpolado(np.linspace(1, count, count)))
    plt.ylabel(desc1)
    plt.show()

    z = array(z)
    r = 0.0
    for i in range(len(x)):
        c = 1.0
        d = 1.0
        for j in range(len(x)):
            if (i != j):
                c = c * (z - x[j])
                d = d * (x[i] - x[j])
            r = r + y[i] * (c / d)
        return r


quest_1 = grafico_lagrange(preço_barroca, vagas_barroca, 0.5, "vagas")
print('Primeira questao:',quest_1)
quest_2 = grafico_lagrange(preço_barroca, areaUtil_barroca, 0.5,"Area util")
print('Segunda questao:',quest_2)
quest_3 = grafico_lagrange(preço_barroca, iptu_barroca, 0.5,"Valor IPTU")
print('Terceira questao:',quest_3)



