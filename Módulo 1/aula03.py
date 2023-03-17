# variáveis #
# Python não tem comando para criar uma variável
# A variável é criada no momento que vc atrtibui valor à ela;

# x != 5;
x = 5  # x recebe o valor 5
y = 3.5 # recebe um valor float
z = 1+2j # reecebe um numero complexo

w = 'Ezequiel' # não faz diferença a aspas simples ou dupla.
w = "Ezequiel" 

# Variáveis podem ir de A-z, 0-9 e o _
# Python é case sensiive: altura, Altura, ALTURA (todas são variáveis diferentes);

h, j , l = 1, 2 ,3
print(h)
print(j)
print(l)

a = b = c = 'Python'
print(a)
print(b)
print(c)

m = w + ' está estudando ' + a
print(m)

f = j + x # j=2 e x=5
print(f)

r = a + y #TypeError: can only concatenate str (not "int"/"float") to str
print(h)  # Python não pode concatenar uma string com um número 

# Python é uma linguagem de tipagem forte pois ela não permite a concatenação de variáveis com valores diferentes( ex: string e int )
# E é dinâmica, pois da pra alterar o valor da variável a qualquer momento no código 