# рекурсия 5
box = [10, 20, 30, 7]
key = 25
def findkey(box, key):
    if len(box) == 0:
        return False
    firstelem = box[0]
    restelem = box[1:]
    if firstelem == key:
        return True
    else:
        firstelem = findkey(restelem, key)
        return firstelem
print(findkey(box, key))
