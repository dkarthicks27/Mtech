def getHash(key):
    total = 0
    for i in str(key):
        total += ord(i)

    return total % 10


# print(getHash('karthick'))

# Hash collision


class KarthickDict:
    def __init__(self, n=10):
        self.arr = [None] * n

    def setter(self, key, value):
        idx = getHash(key)
        print(f"idx position of key: {key} is {idx}")
        self.arr[idx] = value
        print(self.arr)
        print("\n\n")

    def getter(self, key):
        idx = getHash(key)
        return self.arr[idx]

 
newDict = KarthickDict()


newDict.setter('karthick', (34, 35))
newDict.setter('sashvathaman', (99, 99))
newDict.setter('sakthi', (8, 9))


print(newDict.getter('karthick'))