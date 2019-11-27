def ex_16():
    num_1 = int(input("Digite o Primeiro numero: "))
    num_2 = int(input("Digite o Segundo numero: "))  
    if(num_1 > num_2 ):
        print("O numero MAIOR e {}".format(num_1))
    elif(num_2 > num_1):
        print("O numero MAIOR e {}".format(num_2))
    else:
        print("Sao Iguais.")


def ex_17():
    num_1 = int(input("Digite o Primeiro numero: "))
    if(num_1 > 0):
        print("Valor e POSITIVO.")    
    elif(num_1 < 0):
        print("Valor e NEGATIVO.")  
    else:
        print("Valor e 0")

def ex_18():
    sexo = input("Digite uma letra F ou M ").upper().strip()      
    if(sexo == "M"):
        print("M - Masculino") 
    elif(sexo == "F"):
        print("F - Feminino")
    else:
        print("Sexo Inválido")

def ex_19():
    letra=input("Digite uma Letra ").upper().strip()
    vogais = ["A", "E", "I", "O", "U"]
    if(letra in vogais):
        print("isto e uma vogal {} ".format(letra))
    elif(letra not in vogais):
        print("isto e uma consoante {} ".format(letra))
    else:
        print("Valor digitador incorreto.")  

def ex_20():
    notas=[]
    media=0.0
    for i in range(0,2):
        notas.append(float(input("Digite NOta{}: ".format(i+1))))
    media=sum(notas)/len(notas)
    if(media >= 7.0 and media <= 9.9):
        print("Aprovado")
    elif(media<7.0):
        print("Reprovado")
    elif(media == 10.0):
        print("Aprovado com Distinção")
    print(media)

def ex_21():
    numero =[]
    for i in range(0,3):
        numero.append(float(input("Digite um Numero{}: ".format(i+1))))
    print(max(numero))

def ex_22():
    numero =[]
    for i in range(0,3):
        numero.append(int(input("Digite um Numero{}: ".format(i+1))))    


ex_22()