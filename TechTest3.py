queries = [
  ["ADD_FILE", "/file-a.txt", "4"],
  ["ADD_FILE", "/file-a.txt", "8"],
  ["ADD_FILE", "/dir-a/dir-c/file-b.txt", "11"],
  ["ADD_FILE", "/dir-a/dir-c/file-c.txt", "1"],
  ["ADD_FILE", "/dir-b/file-f.txt", "3"],
  ["GET_FILE_SIZE", "/file-a.txt"],
  ["GET_FILE_SIZE", "/file-c.txt"],
  ["MOVE_FILE", "/dir-b/file-f.txt", "/dir-b/file-e.txt"],
  ["MOVE_FILE", "/dir-b/file-a.txt", "/dir-b/file"],
  ["MOVE_FILE", "/file-a.txt", "/dir-b/file-e.txt"]
]

def solution(queries):

    #List for Storages move
    NewBase = []
    dirr = []
    res = []

    for data in queries:

        if data[0] == "ADD_FILE" and data[1] not in dirr:
            NewBase.append([data[1],data[2]])
            dirr.append(data[1])
            res.append("created")

        elif data[0] == "ADD_FILE" and data[1] in dirr:
            NewBase[dirr.index(data[1])] = (data[1], data[2])
            res.append("overwritten")

        elif data[0] == "GET_FILE_SIZE" and data[1] not in dirr:
            res.append("")

        elif data[0] == "GET_FILE_SIZE" and data[1] in dirr:
            x = NewBase[dirr.index(data[1])][1]
            res.append(x)

        elif data[0] == "GET_FILE_SIZE" and data[1] in dirr:
            x = NewBase[dirr.index(data[1])][1]
            res.append(x)

        elif data[0] == "MOVE_FILE" and data[1] in dirr and data[2] not in dirr:
            dirr[dirr.index(data[1])] = data[2]
            res.append("true")

        elif data[0] == "MOVE_FILE" and data[1] not in dirr or data[2] in dirr:
            res.append("false")

    return res
print(solution(queries))