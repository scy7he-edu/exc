# рекурсия 4
mylist = [1, 10, 3, 5]
def findmax (mylist):
    firstnum = mylist[0]
    restnums = mylist[1:]
    if len(mylist) == 1:
        return firstnum
    submax = findmax(restnums)
    if firstnum > submax:
        return firstnum
    else:
        return submax
print(findmax(mylist))