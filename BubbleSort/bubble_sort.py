def main():
    assert(bubble_sort([5, 10, 8, 7, 2]) == [2, 5, 7, 8, 10])
    assert(bubble_sort(['j', 'z', 's', 'a', 'l']) == ['a', 'j', 'l', 's', 'z'])

def swap(array: list, first: int, second: int):
	copy = array[first]
	array[first] = array[second]
	array[second] = copy
	return array

def bubble_sort(array: list):
    size = len(array)
    swapped = True
    while swapped:
        swapped = False
        for index in range(size - 1):
            if array[index] > array[index + 1]:
                swap(array, index, index + 1)
                swapped = True
    return array

if __name__ == '__main__':
    main()