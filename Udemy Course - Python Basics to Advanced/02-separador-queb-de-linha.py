#\r\n CRLF é a quebra de linha nativa do Windows
#\n LF sistema baseado Unix (Linux, mac)
print(12, 34, sep="-", end="\r\n"); #sep="" serve para definir o separador
print(56, 78, sep='-', end="\n"); #end="\n" serve para quebrar a linha
print(9, 10, sep='-', end="\n");
#exemplo1
print(1, 2, 3, sep="-", end="\n --- \n")
print(1, 2, 3, sep="_", end="\n")

#revisão
print(1, 2, sep = '-')