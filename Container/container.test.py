from container import *

def main():
    insertTest()

def insertTest():
    print('Container Insert Test \n')
    insert_test = Container()
    for count in range(20):
        insert_test.insert(count)
    assert(insert_test.count() == 20)
    print('Container Insert Test Passed \n')

if __name__ == '__main__':
	main()