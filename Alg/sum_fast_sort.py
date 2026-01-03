arr = [2, 4, 6]
arr_s = 0

def findsum(arr):
    if len(arr) == 0:
        return 0
    else:
        firstelem = arr[0]
        restelem = arr[1:]
        arr_s = firstelem + findsum(restelem)
        return arr_s
    
print(f'Values summary is {findsum(arr)}')

def findlen(arr):
    return 0 if arr == [] else 1 + findlen(arr[1:])

print(f'Values count is {findlen(arr)}')

def higest(arr):
    if arr == []:
        return 0
    else:
        max_val = arr[0]
        restelem = arr[1:]
        if max_val < higest(restelem):
            max_val = higest(restelem)
    return max_val

print(f'Max value is {higest(arr)}')