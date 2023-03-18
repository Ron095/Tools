queries = [["ADD", "1"],["ADD", "2"],["ADD", "5"],["ADD", "2"],
    ["EXISTS", "2"],["EXISTS", "5"],["EXISTS", "1"],["EXISTS", "4"],["EXISTS", "3"],["EXISTS", "0"]]

b = [["EXISTS","0"],
 ["EXISTS","10"],
 ["ADD","2"],
 ["ADD","3"],
 ["ADD","9"],
 ["EXISTS","3"],
 ["EXISTS","4"],
 ["EXISTS","9"],
 ["EXISTS","10"],
 ["ADD","10"],
 ["ADD","0"],
 ["EXISTS","0"],
 ["EXISTS","1"],
 ["EXISTS","2"],
 ["EXISTS","3"],
 ["EXISTS","4"],
 ["EXISTS","9"],
 ["EXISTS","10"],
 ["EXISTS","11"]]


def solution(queries):
    NumberAdds = []
    listFin = []
    for i in queries:
        if i[0] == "ADD":
            NumberAdds.append(i[1])
            listFin.append("")
        elif i[0] == "EXISTS" and i[1] in NumberAdds:
            listFin.append("true")
        elif i[0] == "EXISTS" and i[1] not in NumberAdds:
            listFin.append("false")
    return listFin

print(solution(b))



