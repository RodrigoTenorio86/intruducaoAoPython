

def ex_01():
    ips = open("ip.txt","r")

    ip_invalidos=[]
    ip_validos=[]
    for ip in ips:
        ip_linha = ip.split()
        for ip_campo in ip_linha:
            ip_numero = ip_campo.split('.')
#            ip_numero = [int(i) for i in ip_numero]
           
    





    ips.close

ex_01()