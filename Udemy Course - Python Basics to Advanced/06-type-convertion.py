# Conversão de tipos, coerção, type convertion, typecasting, coercion
# É o ato de converter um tipo em outro

# Tipos imutáveis e primitivos:
# str, int, float, bool

print(int('1'), type(int('1'))) #Exemplo de coerção de str para int
print(int('1') + 1)
print(float('1.2') + 1)

print(bool('')) #Uma string vazia é considerada False
print(bool(' ')) #Uma string com algo é considerada True

print(str(11) + 'b') #Coerção de int para str, para ser possível concatenar(juntar).