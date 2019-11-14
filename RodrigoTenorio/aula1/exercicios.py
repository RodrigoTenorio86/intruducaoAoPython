import math


def ex_01():
    metro =int(input("Digite valor em Metro? "))
    centimetro = metro * 100
    print("Valor em centímetros {}".format(centimetro))

def ex_02():
    raio =float(input("Digite o raio de Circulo: "))
    area_circulo = math.pi * math.pow(raio,2)
    print("Area do Circulo {}".format(area_circulo))

def ex_03():
    lado = float(input("Digite valor do lado do Quadrado? "))
    area_quadrado = lado * lado 
    print("Area do Quadrado {} e seu valor em dobro e {}".format(area_quadrado,area_quadrado*area_quadrado))

def ex_05():
    valor_hora = float(input("Digite valor ganho por Hora "))
    hora_mes   = float(input("Digite quantas horas de trabalho em um mes? "))
    salario_mes = valor_hora * hora_mes
    print("Valor de Salario do Mes {}".format(salario_mes))

def ex_06():
    farenheit = float(input("Digite valor em Farenheit: "))
    celsius   = (5 * (farenheit - 32)/9)
    print("Valor da Temperatura em Celsius {}".format(celsius))

def ex_07():
    inteiro_1 = int(input("Digite Primeiro Numero Inteiro: "))
    inteiro_2 = int(input("Digite Segundo Numero Inteiro: "))
    real      = float(input("Digite um Numero Real: "))
    valor_a = (inteiro_1 * inteiro_1) * (inteiro_2 /2)
    valor_b = (math.pow(inteiro_2,3) + real)
    valor_c = math.pow(real,3)
    print("o produto do dobro do primeiro com metade do segundo .RESP: {}".format(valor_a))
    print("a soma do triplo do primeiro com o terceiro. {}".format(valor_b))
    print("o terceiro elevado ao cubo. {}".format(valor_c))

ex_07()
