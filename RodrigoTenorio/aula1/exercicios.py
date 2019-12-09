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
    lado = float(input("Digite valor de um dos lados do Quadrado? "))
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

def ex_08():
    altura = float(input("Digite sua Altura: "))
    sexo   = input("Digite seu Sexo (M) para masculino ou (F) para Feminino: ")
    peso_ideal = 0.0
    if(sexo.upper() == "M"):
        peso_ideal = (72.7 * altura) - 58
    elif(sexo.upper() == "F"):
        peso_ideal = (62.1 * altura) - 44.7
    else:
        print("Valor incorreto para sexo.")    
    print("Peso Ideal e {:.02f}".format(peso_ideal))


def ex_09():
    peso_peixe = float(input("Qual peso do Peixe: "))
    if(peso_peixe > 50):
        excedente = peso_peixe - 50
        multa = excedente * 4
        print("Peso do peixe em excesso {} e valor Multa R${}".format(excedente,multa))
    else:
        print("Peso dentro dos limites.")

def ex_10():
    valor_hora = float(input("Digite valor ganho por Hora "))
    hora_mes   = float(input("Digite quantas horas de trabalho em um mes? "))
    salario_bruto = valor_hora * hora_mes
    ir   = salario_bruto * 0.11
    inss = salario_bruto * 0.08
    sind = salario_bruto * 0.05
    salario_liq = salario_bruto - (ir+inss+sind)

    print("Valor de Salario Liquido do mes {}".format(salario_liq))


def run():
    ex_01()
    ex_02()
    ex_03()
    ex_05()
    ex_06()
    ex_07()
    ex_08()
    ex_09()
    ex_10()