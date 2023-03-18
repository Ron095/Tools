import textwrap
#eliminando elementos del inicio y el final
a = [3,4,2,4,38,4,5,3,2]
def solution(a):
    res = a[:]
    while res and res[0] != res[-1]:
        res[1:-1] = res
    return res


#con split separamos cada elemnto del string en una lista, y luego usamos join para que estas sean separads por espacio " "
line = "def      m   e  gaDifficu     ltFun        ction(x):"
def solution1(code):
    return " ".join(code.split())



#replace \t por espacios en blanco. en este caso esta multiplicado por 4 asi q los reemplaza por 4 espacios en blanco
x = "\treturn False".replace("\t",4*" ")



feedback = "This is an example feedback"
size = 8
#Con textwrap.wrap(feedback,size) tu puedes convertir en lineas con una cantidad limite de caracteres colocando el tamanio en size
def solution2(feedback, size):
    return textwrap.wrap(feedback, size)



#con la parte de word[::-1] la palabra word se escribe alrevez
word = "aibohphobia"
def solution3(word):
    return word == word[::-1]



#for this you need a table to the same size of key. this table is created with the command maketrans and the key is our table witch characters to change
#key parameter and table it must be the same lenght
password = "iamthebest"
kEy = "zabcdefghijklmnopqrstuvwxy"
def solution4(password, key):
    table = str.maketrans("abcdefghijklmnopqrstuvwxyz",key)
    return password.translate(table)

