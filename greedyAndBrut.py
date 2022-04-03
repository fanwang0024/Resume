#student ID:29341825
#Name: Ivan(Fan Wang)

def readFile(fileName):
    file = open(fileName,'r')
    table = []
    for line in file:
        line = line.strip()
        line = line.split(' ')
        table.append(line)
    file.close()
    return table

def greedy(list):
    for line in range(len(list)):
        for item in range(len(list[line])):
            if list[line][item] == 'X':
                possible = ['0','1','2','3']
                X=[line-1,line-1,line-1,line,line,line+1,line+1,line+1]
                Y=[item-1,item,item+1,item-1,item+1,item-1,item,item+1]
                listOfPos=aroundCoordinate(list,line,item)
                for index in range(len(listOfPos)):
                    if checkAround(list,X[listOfPos[index]],Y[listOfPos[index]]) in possible:
                        possible.remove(checkAround(list,X[listOfPos[index]],Y[listOfPos[index]]))
                list[line][item] = possible[0]
            else:
                continue
    return list
##Getting the coordinate of valid square around the square which user wants to check.
def aroundCoordinate(list,x,y):  
    X=[x-1,x-1,x-1,x,x,x+1,x+1,x+1]
    Y=[y-1,y,y+1,y-1,y+1,y-1,y,y+1]
    coordinate=[]
    for i in range(len(X)):
        if (X[i] >= 0) and (X[i] < len(list)):
            if (Y[i] >= 0) and (Y[i] < len(list[0])):
                coordinate.append(i)
            else:
                continue
        else:
            continue
    return coordinate
            
##Getting the impossible number from checking around square.If every number is possible,return -1.
def checkAround(list,r,c):
    if list[r][c] == '0':
        return '0'
    elif list[r][c] == '1':
        return '1'
    elif list[r][c] == '2':
        return '2'
    elif list[r][c] == '3':
        return '3'
    else:
        return '-1'
def checkAround_2(list,r,c):
    if list[r][c] == 0:
        return 0
    elif list[r][c] == 1:
        return 1
    elif list[r][c] == 2:
        return 2
    elif list[r][c] == 3:
        return 3
    else:
        return -1

def bruteForce(list):
    counter=0
    X=[]#The list of the raw of squares which equals to 'X'
    Y=[]#The list of the colum of squares which equals to 'X'
    #Recording the coordinate of the square which is equal to 'X'
    for line in range(len(list)):
        for item in range(len(list[line])):
            if list[line][item] == 'X':
                counter+=1#The counter of squares which equals 'X'
                X.append(line)
                Y.append(item)
    #Generating all possible solution of this quilt.
    allResults=possibleResults(counter)
    validReults=[]
    #Checking if each possible solution is valid,if it is,append it to a new list called validResults.
    for k in range(len(allResults)):
        for i in range(len(allResults[k])):
            list[X[i]][Y[i]]=allResults[k][i]
            checker=0
        for i in range(len(allResults[k])):#In this case,the length of allResults[k] equals the length of list X and Y
            XC=[X[i]-1,X[i]-1,X[i]-1,X[i],X[i],X[i]+1,X[i]+1,X[i]+1]
            YC=[Y[i]-1,Y[i],Y[i]+1,Y[i]-1,Y[i]+1,Y[i]-1,Y[i],Y[i]+1]
            validPos=aroundCoordinate(list,X[i],Y[i])
            for index in range(len(validPos)):
                if checkAround_2(list,XC[validPos[index]],YC[validPos[index]]) == list[X[i]][Y[i]]:
                    checker+=1
                else:
                    continue
        if checker == 0:
            validReults.append(allResults[k])
    #Getting the number of colors of every usable result.
    for r in range(len(validReults)):
        listOfNumOfC=[]
        noOfColors=0
        existNum=[]
        for c in range(len(validReults[r])):
            if (validReults[r][c] == '0') and ('0' not in existNum):
                noOfColors+=1
                existNum.append('0')
            elif (validReults[r][c] == '1') and ('1' not in existNum):
                noOfColors+=1
                existNum.append('1')
            elif (validReults[r][c] == '2') and ('2' not in existNum):
                noOfColors+=1
                existNum.append('2')
            elif (validReults[r][c] == '3') and ('3' not in existNum):
                noOfColors+=1
                existNum.append('3')
        listOfNumOfC.append(noOfColors)
    min=0
    for q in range(1,len(listOfNumOfC)):
        if listOfNumOfC[q] < listOfNumOfC[min]:
            min=q
    print(validReults[min])
    for o in range(len(X)):
        list[X[o]][Y[o]]=str(validReults[min][o])
    return list
        


def testFile(list):
    X=[]#The list of the raw of squares which equals to 'X'
    Y=[]#The list of the colum of squares which equals to 'X'
    #Recording the coordinate of the square which is equal to 'X'
    for line in range(len(list)):
        for item in range(len(list[line])):
            if list[line][item] != '-':
                X.append(line)
                Y.append(item)
    checker=0
    for i in range(len(X)):#In this case,the length of allResults[k] equals the length of list X and Y
            XC=[X[i]-1,X[i]-1,X[i]-1,X[i],X[i],X[i]+1,X[i]+1,X[i]+1]
            YC=[Y[i]-1,Y[i],Y[i]+1,Y[i]-1,Y[i]+1,Y[i]-1,Y[i],Y[i]+1]
            validPos=aroundCoordinate(list,X[i],Y[i])
            for index in range(len(validPos)):
                if checkAround_2(list,XC[validPos[index]],YC[validPos[index]]) == list[X[i]][Y[i]]:
                    checker+=1
                else:
                    continue
    if checker == 0:
        return 'valid'
    else:
        return 'Invalid'

            
def possibleResults(n):
    allResults=[]
    for k in range(4**n):
        allResults.append(getAllResults(k,n))
    return allResults
                    
def getAllResults(num,noOfSquares):
    result=[0]*noOfSquares
    k=0
    while num>0:
        result[k]=num%4
        num=num//4
        k+=1
    return result



def printPretty(file):
    for r in range(len(file)):
        for c in range(len(file[r])):
            print(file[r][c],end = " ")
        print()


def menu():
    while True:
        print('Hi!How can I help you?')
        print('1.read file')
        print('2.Apply greedy approach')
        print('3.Apply brute force approach')
        print('4.Test quilt')
        print('5.Exit')
        userChoice = input('Please Enter the number of your choice:')
        if userChoice == '1':
            fileName=input('Please enter the name of the file:')
            a = readFile(fileName)        
            goOn=input('\nType anything to continue...\n')
        
        elif userChoice == '2':
            fileName=input('Please enter the name of the file:')
            s = readFile(fileName)       
            print('\nOriginal quilt:\n')
            printPretty(s)
            print('\nAfter applying greedy approach:\n')
            d = greedy(s)
            printPretty(d)
            goOn=input('\nType anything to continue...\n')

        elif userChoice == '3':
            fileName=input('Please enter the name of the file:')
            q = readFile(fileName)       
            print('\nOriginal quilt:\n')
            printPretty(q)
            print('\nAfter applying brute force approach:\n')
            w = bruteForce(q)
            printPretty(w)
            goOn=input('\nType anything to continue...\n')

        elif userChoice == '4':
            askUser=1
            while askUser == 1:
                fileName=input('Please enter the name of the file:')
                c = readFile(fileName)
                e=testFile(c)
                print('\n',e,'\n')
                askUser=int(input('would you like to test another file?[1]yes [2]no'))
            goOn=input('\nType anything to continue...\n')

        elif userChoice == '5':
            DCheck = input('\nAre you sure to leave?[1]Yse [2]No\n')
            if DCheck == '1':
                print('See you next time!\n')
                break
            elif DCheck == '2':
                print('\nWelcome back!\n')
        else:
            print('\nerror,please enter valid number!\n')

if __name__=='__main__':
    menu()    
