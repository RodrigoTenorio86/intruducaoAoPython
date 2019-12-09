def ex_29():
    valor_valido = True
    while valor_valido :
        valor = int(input("Digite uma Nota, entre Zero e Dez "))
        if(valor >= 0 and valor <= 10):
            valor_valido = False
            print("Valor Valido.")
        else:
            print("Valor Invalido {}".format(valor))

def ex_39():
    for i in range(1,11):
        print("{}".format(i))
    for i in range(1,11):
        print("{}".format(i,end=""))

def ex_40():
    numeros=[]
    for i in range(0 ,5):
        numeros.append( float(input("Digite um Numero: ")))
    print("O maior Numero: {}".format(max(numeros)))


def ex_41():
    numeros = []
    for i in range(0,5):
        numeros.append(float(input("Digite numero: ")))
    print("Soma: {}".format(sum(numeros)))
    print("Media: {0:.2f}".format(sum(numeros)/len(numeros)))

def ex_42():
    for i in range(1,51):
        if(not i%2 == 0):
            print("Numero Impar {}".format(i))

def ex_44():
    qtd_turma = int(input("Digite quantidade de Turma: "))
    qnt_aluno_por_turma = []
    if(qtd_turma > 0):
        i = 0
        while i < qtd_turma:
            qnt_aluno = int(input("Digite quantidade de alunos nesta Turma: "))
            if(qnt_aluno <= 40):
                qnt_aluno_por_turma.append(qnt_aluno)
                i = i +1
            else:
                print("Esta Turma Nao pode ter mais de 40 Alunos.")
    print(qnt_aluno_por_turma)
    print("A media de Alunos por Turma e {0:.2f}".format(sum(qnt_aluno_por_turma)/len(qnt_aluno_por_turma)))


def ex_45():
    qtd_cd = int(input("Digite quantidade de CD: "))
    valor_cada_cd = []
    if(qtd_cd > 0):
        for i in range(0 ,qtd_cd):
            valor_cada_cd.append(float(input("Digite valor do CD: ")))
    print("Valor Total investido: {0:.2f}".format(sum(valor_cada_cd)))
    print("Valor Medio: {0:.2f}".format(sum(valor_cada_cd)/len(valor_cada_cd)))
    
def ex_46():
    temperaturas=[]
    condicao = True
    while condicao:
        temperatura = input("Digite valor da Temperatura ou F para fim. ")
        if(temperatura.upper().strip() != 'F'):
            temperaturas.append(float(temperatura))
        else:
            condicao =False
    print("Temperatura Minima e {}C".format(min(temperaturas)))
    print("Temperatura Maximo e {}C".format(max(temperaturas)))
    print("Temperatura Media: {}C".format(sum(temperaturas)/len(temperaturas)))
    print(temperaturas)
            

def ex_47():
    num = int(input("Digite um numero inteiro positivo: "))
    primo="Primo"
    if(num <= 1):
        primo="Não é um número Primo."
    for i in range(2,num):
        if (num%i== 0 and i != 1):
            primo="Não é um número Primo."
    print(primo)

def ex_48():
    num = int(input("Digite um Numero Inteiro Posistivo para gera uma lista dos Numeros primos: "))
    for i in range(1, num):
        for j in range(2,i):
            if(i%j==0 and i != 1):
                print(i)


ex_48()