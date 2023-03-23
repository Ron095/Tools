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

#print(solution15(studentsss))




#with this you sum each element in the list ids but individuality
#for example the first number = '529665' = 5+2+9+6+6+5 and return true
#if the sum of all elements is divisible by kh=3
ids = [529665, 909767, 644200]
kh = 3
def solution16(ids, kh):
    digitSum = lambda Id: sum(float(i) for i in str(Id))
    sm = 0
    for questionId in ids:
        sm += digitSum(questionId)
    return sm % kh == 0

#print(solution16(ids,kh))

#Problem about change number that contained zero nad it must be stay in ascending way. if you want to se the problem, check in your folder ARCHIVOS IMPORTANTEA and see the picture PRACTICE PYTHON
def flip(i):
    flipper = int(''.join(str(i)[::-1]))
    if i == flipper:
        ans = False
    else:
        ans = True
    return (flipper, ans)
def is_asacending(lstt):
    res = all(i<j for i,j in zip(lstt, lstt[1:]))
    return res
def solution17(lstt):
    if is_asacending(lstt)==True:
        return True
    else:
        NewList = []
        ans = []
        for i in lstt:
            CopyList = lstt.copy()
            y = lstt.index(i)
            CopyList[y] = flip(i)[0]
            NewList.append(CopyList)
            if is_asacending(CopyList):
                ans.append(True)
            else:
                ans.append(False)
        if True in ans:
            return True
        else:
            return False


#print(solution17([1,5,10,20]))
#print(solution17([1,3,900,10]))
#print(solution17([13,31,30]))
#print(solution17([222,214,333]))



#Sawtooth secuence

#with this function check if either numbers have the seme sign
def samesign(a, b):
    if a / abs(a) == b / abs(b):
        return True
    else:
        return False

def countSawSubarrays(arr):
    n = len(arr) #give the lenght of array
    if n < 2:
        return 0  #if the array lenght if smaller than 2 then return 0 directly like response becasue you only have sawtooth secuence with two o more points on the array

    #but when lenght of n is greater than two, then:
    s = 0 #is a count to start in Zero
    e = 1 #is a count to start in One
    count = 0 #is a count to acumulate a value

    while (e < n): #this bucle it'll be repeated until "e" is less than "n"
        sign = arr[e] - arr[s] #wiht this line we subtract 'e' element on array with 's' element, in this case you can look like the present number with the previous
        while (e < n and arr[e] != arr[e - 1] and samesign(arr[e] - arr[e - 1], sign)):
            sign = -1 * sign
            e += 1
        size = e - s
        if (size == 1):
            e += 1
        count += (size * (size - 1)) // 2
        s = e - 1
        e = s + 1
    return count


arr2 = [1,2,1,2,1]



#print(countSawSubarrays(arr2))

#kadane's algorithm to resolve the maximum sum subarray problem
def max_subarray(numbers):
    """Find the largest sum of any contiguous subarray."""
    best_sum = 0
    current_sum = 0
    for x in numbers:
        current_sum = max(0, current_sum + x)
        best_sum = max(best_sum, current_sum)
    return best_sum

def MaxSum_subarray(numbers):
    max_sum = numbers[0]
    current_sum = max_sum

    max_start = 0
    max_end = 0
    current_start = 0

    for i in range(len(numbers)):
        current_sum = current_sum + numbers[i]
        current_end = i
        if current_sum < 0:
            current_sum = 0

            #start a new sequence from next element
            current_start = current_end + 1

        if max_sum < current_sum:
            max_sum = current_sum
            max_start = current_start
            max_end = current_end

    NewArray = numbers[max_start:max_end+1]

    return max_sum, NewArray

print(MaxSum_subarray([-2,-3,4,-1,-2,5,-3]))
print(MaxSum_subarray([-3,1,-8,12,0,-3,5,-9,4]))

