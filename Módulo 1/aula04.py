# strings #

print("olá mundo")
print('olá mundo')

a = 'Curso de Python3'
print(a)

"""comentario""" # não lê quando roda o programa
# essa string não está armazenada na memória, em uma variável
# mas da pra armazenar...

b = """\nOla,
este é um curso de python
espero que goste"""
print(b) # a variável 'b' armazena um texto em bloco, utilizando exatamente as mesmas quebras de linha que o comentário com 3 aspas duplas

# métodos das strings #

# da pra usar mais de um método em uma função
c = ' Ola mundo '
print(c.strip()) # esse método ignora os espaços vazios, antes e depois da frase armazenada na string

d = ' OlA mUnDo '
print(d.lower().strip()) # esse método deixa todas as letras da string minusculas

e = 'ola mundo'
print(e.upper()) # esse método faz o oposto da anterior, deixando ela toda

f = 'hello'
g = 'world'
space = ' '

print(f + space + g)