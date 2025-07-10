def printNumbers(Lrange, Urange):
    #base case
    if Lrange > Urange:
        return
    print(Lrange) #12345
    printNumbers(Lrange + 1, Urange)
    print(Lrange) #54321

printNumbers(1, 10)
