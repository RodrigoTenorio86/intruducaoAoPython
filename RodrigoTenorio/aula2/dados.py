import math
import numbers

def ex_02():
    nome = input("Digite seu Nome: ")
    for letra in nome:
        print(letra)

def ex_03():
    notas = []
    for i in range(1,5):
        notas.append( float( input("Digite nota{} ".format(i))) )
    media = sum(notas) / len(notas)
    print("media da nota {:.02f}".format(media))

def ex_04():
    letras = []
    vogais = ["A", "E", "I", "O", "U"]
    total_consoante = 0
    for i in range(0,10):        
        letras.append( input("Digite uma letra ").upper())
    for consoante in letras:
            if (consoante not in vogais ):
                print(consoante)
                total_consoante = total_consoante +1

    print(total_consoante)   

def ex_05():
    numeros=[]
    par = []
    impar = []
    for i in range(0,20):
        numeros.append(int(input("Digite um numero: ")))
    for numero in numeros:
        if(numero%2==0):
            par.append(numero)
        else:
            impar.append(numero)    
    print(numeros)        
    print(par)
    print(impar)

def ex_06():
    meses=["0","Janeiro","Fevereiro","Marco","Abril","Maio","Junho","Julho","Agosto","Stembro","Outubro","Novembro","Dezembro"]
    dia = int(input("Digite dia do Nascimento: "))
    mes = int(input("Digite mes de Nascimento: "))
    ano = int(input("Digite ano de Nascimento: "))
    print("Data Nascimento {} de {}  de {}".format(dia,meses[mes],ano))


def ex_07():
    turma=[]
    for i in range(0,5):
        alunos = []
        nome_aluno = input("Digite nome do Aluno: ")
        alunos.append(nome_aluno)   
        nota_total = 0   
        for j in range(0,4):
            nota = float(input("Digite notas do aluno {} ".format(nome_aluno)))
            alunos.append(nota)
            nota_total = nota_total + nota
        media= nota_total / 4
        alunos.append(media)
        turma.append(alunos)
    contador = 0
    for i in range(0,5):
        if(turma[i][5] >= 7):
            contador = contador +1
    print("Numero total de alunos com média maior ou igual a 7.0 é {}".format(contador))

def ex_08():
    String_1 = input("Digite uma frase: ")
    String_2 = input("Digite outra frase: ")
    print("String1: {}".format(String_1))
    print("String2: {}".format(String_2))
    frase1 = []
    frase2 = []
    for letra in String_1:
        frase1.append(letra)
    for letra in String_2:
        frase2.append(letra)
    print("Tamanho de {}"" : " "{} caracteres".format(String_1,len(frase1)))
    print("Tamanho de {}"" : " "{} caracteres".format(String_2,len(frase2)))
    if(len(String_1)==len(String_2)):
        print("As duas strings são de tamanhos Igual.")
    else:
        print("As duas strings são de tamanhos diferentes.")
    if(frase1 == frase2):
        print("As duas strings possuem conteúdo Igual.")
    else:
        print("As duas strings possuem conteúdo diferente.")

def ex_09():
    vetor = []
    soma = 0
    multiplicacao = 1
    for i in range(0, 5):
        numero_inteiro = int(input("Digite um Numero Inteiro: "))
        vetor.append(numero_inteiro)
    for num in vetor:
        soma = soma + num
        multiplicacao = multiplicacao * num
    print(" os numero sao: {}".format(vetor))
    print(soma)
    print(multiplicacao)
        
def ex_10():
    pessoas = []
    for i in range(0,5):
        dados = []
        idade = int(input("Digite Idade: "))
        altura = float(input("Digite Altura: "))
        dados.append(idade)
        dados.append(altura)
        pessoas.append(dados)
    pessoas.reverse()
    print(pessoas)


def ex_11():
    A = [x for x in range(10)]
    soma = 0
    for x in A:
        print(x**2) 
        soma= soma + x**2
    print("Soma: ",soma)

def ex_12():
    A = [x for x in range(5,55,5)]
    B = [x for x in range(6,66,6)]
    vetor_misto = []
    for x in range(0, 10):
        vetor_misto.append(A[x])
        vetor_misto.append(B[x])

    print(A)
    print(B)
    print(vetor_misto)
    
        

    
def run():
    ex_02()
    ex_03()
    ex_04()
    ex_05()
    ex_06()
    ex_07()
    ex_08()
    ex_09()
    ex_10()
    ex_11()
    ex_12()  


            


