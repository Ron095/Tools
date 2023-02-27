def Binary (decimal):
    Binary = ""
    while decimal // 2!= 0:
        Binary = str(decimal % 2) + Binary
        decimal = decimal // 2
    return str(decimal) + Binary

Number = int(input("Insert the number you want to convert to binary: "))
print(Binary(Number))

