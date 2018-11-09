import csv
import numpy as np
import matplotlib.pyplot as plt


preço_barroca = []
vagas_barroca = []
areaUtil_barroca = []
iptu_barroca = []
preço_total = []
areaUtil_total = []

f = csv.reader(open('C:/Nova pasta/imobiliaria.csv'), delimiter=';')
for [imovel_Id,tipoImovel,valorImovel,areaRealPrivativa,latitude,longitude,quartos,banho,suites,vagaGaragem,valorCondominio,valorIptu,Cidade,Regiao,Bairro,Endereco] in f:
    if valorImovel != 'valorImovel' and Bairro == 'Alto Barroca':
        preço_barroca.append(int(valorImovel))
    if vagaGaragem != 'vagaGaragem' and Bairro == 'Alto Barroca':
        vagas_barroca.append(int(vagaGaragem))
    if quartos != 'quartos' and Bairro == 'Alto Barroca':
        areaUtil_barroca.append(int(quartos+banho+suites))
    if valorIptu != 'valorIptu' and Bairro == 'Alto Barroca':
        iptu_barroca.append(valorIptu)
    if valorImovel != 'valorImovel':
        preço_total.append(int(valorImovel))
    if quartos != 'quartos':
        areaUtil_total.append(int(quartos + banho + suites))

def Preço_VagasGaragem_barroca():
    x = np.array(preço_barroca)
    y = np.array(vagas_barroca)
    p1 = np.polyfit(x, y, 1)
    yfit = p1[0] * x + p1[1]
    yresid = y - yfit
    SQresid = sum(pow(yresid, 2))
    SQtotal = len(y) * np.var(y)
    R2 = 1 - SQresid / SQtotal

    plt.plot(x, y, 'o')
    plt.plot(x, np.polyval(p1, x), 'g--')
    plt.xlabel("Preço")
    plt.ylabel("Vagas")
    plt.show()

def Preço_areaUtil_barroca():
    x = np.array(preço_barroca)
    y = np.array(areaUtil_barroca)
    p1 = np.polyfit(x, y, 1)
    yfit = p1[0] * x + p1[1]
    yresid = y - yfit
    SQresid = sum(pow(yresid, 2))
    SQtotal = len(y) * np.var(y)
    R2 = 1 - SQresid / SQtotal

    plt.plot(x, y, 'o')
    plt.plot(x, np.polyval(p1, x), 'g--')
    plt.xlabel("Preço")
    plt.ylabel("Area util")
    plt.show()

def Preço_iptu():
    print('Tratar os dados da coluna de IPTU')

def Preço_areaUtil_total():
    x = np.array(preço_total)
    y = np.array(areaUtil_total)
    p1 = np.polyfit(x, y, 1)
    yfit = p1[0] * x + p1[1]
    yresid = y - yfit
    SQresid = sum(pow(yresid, 2))
    SQtotal = len(y) * np.var(y)
    R2 = 1 - SQresid / SQtotal

    plt.plot(x, y, 'o')
    plt.plot(x, np.polyval(p1, x), 'g--')
    plt.xlabel("Preço")
    plt.ylabel("Area util")
    plt.show()

Preço_VagasGaragem_barroca()
Preço_areaUtil_barroca()
Preço_iptu()
Preço_areaUtil_total()
