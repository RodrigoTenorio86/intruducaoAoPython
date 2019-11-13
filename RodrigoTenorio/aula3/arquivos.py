

def ex_01():
    ips = open("ip.txt","r")

    ip_invalidos=[]
    ip_validos=[]
    for ip in ips:
        ip_linha = ip.split()
        for ip_campo in ip_linha:
            ip_numero = ip_campo.split('.')
            for i in ip_numero:
                i = int(i)
                if(i >255):
                    ip_invalidos.append(ip_numero)
#            ip_numero = [int(i) for i in ip_numero]
           
    
    for j in ip_invalidos:
        print(j)




    ips.close

ex_01()