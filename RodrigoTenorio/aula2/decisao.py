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
        numero.append(int(input("Digite um Numero inteiro positivo {}: ".format(i+1)))) 
    numero.sort(key=int, reverse=True)
    print(numero)

def ex_23():
    palavra = input("Digitar M-matutino ou V-Vespertino ou N- Noturno ") 
    palavra = palavra.strip().upper()
    if(palavra == "M"):
        print("Bom Dia!")
    elif(palavra == "V"):
        print("Boa Tarde!")
    elif(palavra == "N"):
        print("Boa Noite!")
    else:
        print("Valor Invalido!!!")
       
def ex_25():
    dia_da_semana = int(input("Digite dia correspondente da Semana: "))
    semana = [" ","Domingo", "Segunda-feira", "Terca-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sabado"]
    if(1 <= dia_da_semana <= 7):
        print(semana[dia_da_semana]) 
    else:
        print("Valor Invalido!!!")

def ex_26():
    notas = []
    for i in  range(0,2):
        notas.append(float(input("Digite nota do Aluno ")))
    media = round( sum(notas)/ len(notas),1)
    if(9.0 <= media <= 10.0):
        conceito = "A"
    elif(7.5  <= media <= 9.0):
        conceito = "B"
    elif( 6.0<= media <= 7.5):
        conceito ="C"
    elif(4.0<= media <= 6.0 ):
        conceito="D"
    else:
        conceito="E"
    conceito_aprovado=["A","B","C"]  
    if(conceito in conceito_aprovado):
        msg = "APROVADO"
    else:
        msg = "REPROVADO"
    print("Notas: {}".format(notas))
    print("Media: {}".format(media))    
    print(conceito)
    print(msg)

def run():
    ex_16()
    ex_17()
    ex_18()
    ex_19()
    ex_20()
    ex_21()
    ex_22()
    ex_23()
    ex_25()
    ex_26()