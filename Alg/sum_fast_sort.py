class RecursiveArray:
    def __init__(self, arr):
        self.arr = arr

    def find_sum(self, arr=None):
        if arr is None:
            arr = self.arr
        
        if len(arr) == 0:
            return 0
        else:
            firstelem = arr[0]
            restelem = arr[1:]
            return firstelem + self.find_sum(restelem)

    def find_len(self, arr=None):
        if arr is None:
            arr = self.arr
        return 0 if not arr else 1 + self.find_len(arr[1:])

    def find_highest(self, arr=None):
        if arr is None:
            arr = self.arr
        
        if not arr:
            return 0
        else:
            max_val = arr[0]
            restelem = arr[1:]
            sub_max = self.find_highest(restelem)
            if max_val < sub_max:
                max_val = sub_max
        return max_val

if __name__ == '__main__':
    arr = [2, 4, 6]
    processor = RecursiveArray(arr)
    print(f'Values summary is {processor.find_sum()}')
    print(f'Values count is {processor.find_len()}')
    print(f'Max value is {processor.find_highest()}')