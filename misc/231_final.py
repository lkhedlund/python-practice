def row_by_row(aList):
    for row in aList:
        print(row)

def col_by_col(aList):
    for col in range(len(aList[0])):
        for row in range(len(aList)):
            print aList[row][col]

def findHigher(n, aList):
    new_list = []
    for item in aList:
        if item > n:
            new_list.append(item)
    return new_list

def fileWrite(grades):
    output = open("test3.txt", "w")
    for grade in grades:
        output.write(str(grade) + "\n")
    output.close()

twoDlist = [[1,2,3],[1,2,3]]
oneDlist = [1,2,3,4,5]

row_by_row(twoDlist)
col_by_col(twoDlist)
print(findHigher(2, oneDlist))
fileWrite(oneDlist)
