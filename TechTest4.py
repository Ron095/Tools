import textwrap
import re

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



#Fibonacci
def Fibonnaci(numero:int):
    if numero == 0:
        return 0
    elif numero == 1:
        return 1
    else:
        return Fibonnaci(numero - 2) + Fibonnaci(numero - 1)


#for i in range(10):
    #print(Fibonnaci(i))


#print(Fibonnaci(10))

#con esta alineas un numero en la variable t en un espacio width y con la cantidad de decimales en precision
#utilizando el method format
def solution5(t, width, precision):
    return '{:^{}.{}f}'.format(t, width, precision)
#print(solution5(3.1415, 10, 2))

type = 'bug'
result = 'troubling'

#print('I wondered why the program was %s me. Then\
 #it dawned on me it was a %s .' % (result, type))

match = 12000
site = 'amazon'

#print("%s is so useful. I tried to look\
 #up mobile and they had a nice one that cost %d rupees." % (site, match))



#con este formato se esta organizando cada operacion en un espacio de 10, en el centro ya que tiene el ^
def organized(a, b):
    for i in range(a, b):
        print('{:^10d}{:^10d}{:^10d}{:^10d}'.format(i, i ** 2, i ** 3, i ** 4))
#print(organized(4, 11))



#para reemplazar un valor '%%' por '%' en  una lista s
fgf = "We expect the %f%% growth this week"
def newStyleFormatting(s):
    s1 = re.sub('%%', '{%}', s)
    s3 = re.sub('%[dfgexXocbs]', '{}', s1)
    return re.sub('{%}','%', s3)
#print(newStyleFormatting(fgf))


#para reemplazar varios caracteres de un string utilizando translate
pwd = "0??+0+!!someCommIdhsSt"
#forma 1 con translate
def deletemen6(commit:str):
    UknowChar = ['0','?','+','!']
    return commit.translate({ord(i): None for i in UknowChar})
#print(deletemen6(pwd))

#forma 2 con join
def deletemen7(commit:str):
    return ''.join([i for i in commit if i not in ['0','?','+','!']])
#print(deletemen7(pwd))


#extender listas o unirlas
def solution8(list1, list2):
    res = list1
    res.extend(list2)
    return res
lst1 = [2,2,1]
lst2 = [10,11]
#print(solution8(lst1,lst2))


#para sumar numeros que estan en una posicion par y otros en posicion impar
#forma1
students = [1, 11, 13, 6, 14]
def solution9(students):
    return sum([students[i] for i in range(0,len(students)) if i % 2 == 0]) - sum([students[i] for i in range(0,len(students)) if i % 2 != 0])
#forma2
def solution10(students):
    return sum(students[::2]) - sum(students[1::2])

toDo = [1237, 2847, 27485, 2947, 1, 247, 374827, 22]
k = 3

#eliminando el k elemento y asi sucesivamente, en este caso se eleminal primer tercer
#elemento que es el 27485 y luego cuenta nuevamente siendo el tercer elemento ahora 247
def solution11(k, toDo):
    del toDo[k-1::k]
    return toDo


#mostrando la lista en un string usando format
lst = [1, 2, 3, 4, 5]
def solution12(lst):
    return 'This is your list: {}'.format(lst)
#print(solution12(lst))

#lambdan function (es una funcion qu recibe dos parametros ch y n)
sol13 = lambda ch,n:ch*n
#print(sol13('?',35))


#con la funcion lambda estamos haciendo que se sumen los indices que tienen true en la lista
#y si tienen false se le resta p
def solution14(answers, p):
    questionPoints = lambda i,ans: i+1 if ans=='true' else -p
    res = 0
    for i, ans in enumerate(answers):
        res += questionPoints(i, ans)
        print(res)
    return res


answers = ['true', 'true', 'false', 'true']
p = 2
#print(solution14(answers,p))

#ordenando una lista en funcion de sus apellidos con el metodo sort y dentro de key la funcion lambda
#con el espacio en el split es como que tomamos un estudiante y quedarian tantos elementos
#como palabras tenga su apellido ejemplo ['Jacky','Mon','Simonoff'] es una lista de 3
#elementos. y ponemos el [-1] para que siempre tome el ultimo valor de la derecha que es
#con el que inicia. por lo tanto la funcion sort va a ordenar en funcion del apellido

def solution15(students):
    students.sort(key=lambda name: name.split(' ')[-1])
    return students
studentsss = ["John Smith", "Jacky Mon Simonoff","Lucy Smith", "Angela Zimonova"]

print(solution15(studentsss))