# En la variable 'text' dispones de una cadena de texto
# debes contar las palabras y devolver cuantas vececs se repiten cada una de ellas
# Ejemplo --> 'nada' aparece 2 veces


text = "Creo que a veces es la gente de la que nadie espera nada, la que hace cosas que nadie puede imaginar."




#with this you conver string to lowecase
def ToLowerCAse (text):
    lowrCase = text.lower()
    return lowrCase

#with this you clean the special characters in the string and convert to list
def CleanCharac (Text):
    ClenChart = Text.replace(',','').replace('.','')
    Separate = ClenChart.split(' ')
    return Separate

#wtih this you count any word in the list and return a dictionary with the count number
def CountWords (List):
    dictionary = {}
    for word in List:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    return dictionary


a = ['paula','paula','paula','paula','camila','camila','camila','camila','camila','camila']


print(CountWords(CleanCharac(ToLowerCAse(text))))
