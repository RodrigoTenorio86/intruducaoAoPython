#Autor: RodrigoTenorio

def ex_01():
    ips = open("ip.txt","r")
    ip_invalidos=[]
    ip_validos=[]
    for ip in ips:
        numero=ip.split('.')
        if( int(numero[0]) <= 255 and int(numero[1]) <= 255 and int(numero[2]) <= 255 and int(numero[3]) <= 255):
            ip_validos.append(ip)
        else:
            ip_invalidos.append(ip)

    arq = open("lista_ip.txt","w")
    texto ="[Endereços válidos:]"+"\n"
    arq.write(texto)
    for ip_ in ip_validos:
        arq.write(ip_)
    texto ="\n"+"\n"+"[Endereços inválidos:]"+"\n"
    arq.write(texto)
    for ip_ in ip_invalidos:
        arq.write(ip_)

    ips.close()
    arq.close()

def ex_02():
    relatrio =open("usuario.txt","r")
    usuarios = []
    espaco  = []
    for palavra in relatrio:
        palavra= palavra.split()
        usuarios.append(palavra[0])
        espaco.append(converter_byte_mega( int(palavra[1])))
    relatrio.close()


    arq=open("relatorio.txt","w")
    cabecalho = "ACME Inc.                 Uso do espaço em disco pelos usuários    "+"\n"
    linhas="------------------------------------------------------------------------"+"\n"
    enunciado="Nr. Usuário                       Espaço utilizado           % do uso"+"\n"+"\n"
    arq.write(cabecalho)
    arq.write(linhas)
    arq.write(enunciado)
    con = 0
    while con < len(usuarios):
        arq.write("{}  {}                     {} MB        {}% \n".format(con+1, usuarios[con], espaco[con], porcento_do_uso(sum(espaco), espaco[con]) ) )
        con +=1
    arq.write("\n")    
    arq.write("Espaço total ocupado: {} MB\n".format(sum(espaco)))
    arq.write("Espaço médio ocupado: {} MB".format( round(sum(espaco)/len(espaco),2 )))

    arq.close()

 

def converter_byte_mega(num_bute):
    num_mega = ( num_bute / 1024)/1024
    return  round(num_mega,2)

def porcento_do_uso(total,uso):
    valor = (uso * 100)/total
    return round(valor,2)



    

def run():
    ex_01()
    ex_02()