"""
A way to hold data, not a sophisticated structure
"""
class Container:
    def __init__(self):
        self.__count = 0
        self.__data = [None] * 8 

    def insert(self, element):
        if self.__count == len(self.__data):
            copy = [None] * (self.__count * 2)
            for index in range(self.__count):
                copy[index] = self.__data[index]
            self.__data = copy
        self.__data[self.__count] = element
        self.__count += 1
        return self

    # returns the number of items in the container    
    def count(self):
        return self.__count

    # returns the number of items that equate to element in the container
    def countItems(self, element):
        count = 0
        for data in self.__data:
            if data == element:
                count += 1
        return count

    # removes one of the items that match the element in the container
    # moves the last index of the container to the index of the removed element
    # decrements count by 1
    def removeOne(self, element):
        for index in range(self.__count):
            if data[index] == element:
                data[index] = data[self.__count]
        self.__count -= 1
        return self

    # removes all instances of that element in the container
    def removeAll(self, element):
        count = self.countItems(element)
        for index in range(count):
            self.removeOne(element)
        return self
            

