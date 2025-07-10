def printNumbers(Lrange, Urange):
    #base case
    if Lrange > Urange:
        return
    print(Lrange)
    printNumbers(Lrange + 1, Urange)

printNumbers(1, 10)