def binTodec(binnum):
    decnum=int(binnum, 2)
    return decnum

def octTodec(octnum):
    decnum=int(octnum, 8)
    return decnum

def hexTodec(hexnum):
    decnum=int(hexnum, 16)
    return decnum

def binTooct(binnum):
    decnum=int(binnum, 2)
    return oct(decnum)

def binTohex(binnum):
    decnum=int(binnum, 2)
    return hex(decnum)

def octTobin(octnum):
    decnum=int(octnum, 8)
    return oct(decnum)

def octTohex(octnum):
    decnum=int(octnum, 8)
    return hex(decnum)

def decTobin(decnum):
    return bin(decnum)

def decTooct(decnum):
    return oct(decnum)

def decTohex(decnum):
    return hex(decnum)

def hexTobin(hexnum):   
    decnum=int(hexnum, 16)
    return bin(decnum)

def hexTooct(hexnum):
    decnum=int(hexnum, 16)
    return oct(decnum)

num=input("Enter number : ")
type=input("Enter type of entered num (bin/ oct/ dec/ hex): ")
con=input("To be converted into (bin/ oct/ dec/ hex): ")

if type==con:
    print("Same num system representation NO NEED TO CONVERT")
else:
    print("Result: ")
    fun=type+"To"+con
    if fun=="binTodec":
        newnum=binTodec(num)
        print(newnum)
        
    elif fun=="binTooct":
        newnum=binTooct(num)
        print(newnum)
        
    elif fun=="binTohex":
        newnum=binTohex(num)
        print(newnum)
        
    elif fun=="octTobin":
        newnum=octTobin(num)
        print(newnum)
        
    elif fun=="octTodec":
        newnum=octTodec(num)
        print(newnum)
        
    elif fun=="octTohex":
        newnum=octTohex(num)
        print(newnum)
        
    elif fun=="decTobin":
        newnum=decTobin(num)
        print(newnum)
        
    elif fun=="decTooct":
        newnum=decTooct(num)
        print(newnum)
        
    elif fun=="decTohex":
        newnum=decTohex(num)
        print(newnum)
        
    elif fun=="hexTobin":
        newnum=hexTobin(num)
        print(newnum)
        
    elif fun=="hexTooct":
        newnum=hexTooct(num)
        print(newnum)
        
    elif fun=="hexTodec":
        newnum=hexTodec(num)
        print(newnum)
        
    else:
        print("Invalid type of num! CANNOT BE CONVERTED!")