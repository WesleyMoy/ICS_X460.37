from linked_list import *

def main():
    appendTest()

def appendTest():
    print('Container Insert Test \n')
    append_test = LinkedList()
    for count in range(20):
        append_test.append(count)
    print('Container Insert Test Passed \n')

if __name__ == '__main__':
	main()