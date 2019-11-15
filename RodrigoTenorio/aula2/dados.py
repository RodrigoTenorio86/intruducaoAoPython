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
            if (not consoante  in vogais ):
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

ex_05()