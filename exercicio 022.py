nomec = str(input('Qual seu nome completo?'))
print('Nome:{}'.format(nomec.upper()))
print('Nome:{}'.format(nomec.lower()))
print('Quantidades de caractere:{}'.format(len(nomec.replace(' ',''))))
nomec = nomec.split()
print('Primeiro nome:{}'.format(len(nomec[0])))