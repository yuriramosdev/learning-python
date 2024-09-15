a = 'A'
b = 'B'
c = 1.1

#ARGUMENTO
string = 'a={0} a={0} a={0} b={1} c{2:.2f}'
formato = string.format(a, b, c)

print(formato)

#PARAMETRO NOMEADO
string1 = 'b={nome2} a={nome1} a={nome1} a={nome1} c{nome3:.2f}'
formato1 = string1.format(nome1=a, nome2=b, nome3=c)

print(formato1)