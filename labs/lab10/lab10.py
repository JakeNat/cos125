import timeit


def bubblesort(numlist):
    for i in range(len(numlist)-1):
        temp = numlist[i]
        if numlist[i] > numlist[i+1]:
            numlist[i] = numlist[i+1]
            numlist[i+1] = temp
        for j in range(len(numlist)-1):
            temp = numlist[j]
            if numlist[j] > numlist[j+1]:
                numlist[j] = numlist[j+1]
                numlist[j+1] = temp

            

def selectionsort(numlist):
    for i in range(len(numlist)-1):
        min_index = i
        for j in range(i+1,len(numlist)):
            if numlist[j]<numlist[min_index]:
                min_index=j
        temp = numlist[i]
        numlist[i] = numlist[min_index]
        numlist[min_index] = temp


def is_sorted(numlist):
    for x in range(len(numlist)-1):
        if numlist[x] > numlist[x+1]:
            return False
    return True


def time_bubble_sort():
    init = '''
from __main__ import bubblesort
from __main__ import is_sorted
import random
numlist = []
size = 10000
for i in range(size):
    numlist.append(random.randint(0,size*10))
'''
    
    code = '''
bubblesort(numlist)
print("BUBBLE SORT - IS SORTED: ",is_sorted(numlist))
    '''

    runtime = timeit.timeit(setup=init,stmt=code,number=1)
    print("TIME (secs): ",runtime)


def time_selection_sort():
    init = '''
from __main__ import selectionsort
from __main__ import is_sorted
import random
numlist = []
size = 10000
for i in range(size):
    numlist.append(random.randint(0,size*10))
'''
    
    code = '''
selectionsort(numlist)
print("SELECTION SORT - IS SORTED: ",is_sorted(numlist))
    '''

    runtime = timeit.timeit(setup=init,stmt=code,number=1)
    print("TIME (secs): ",runtime)

def main():

    # UNCOMMENT THE FOLLOWING TWO LINES FOR TASK 1
    time_bubble_sort()
    time_selection_sort()

    # COMMENT OUT THE FOLLOWING LINE FOR TASK 1
    # import random
    # numlist = []
    # size = 1000
    # for i in range(size):
    #     numlist.append(random.randint(0,size*10))
    # bubblesort(numlist)
    # print("IS SORTED: ",is_sorted(numlist))

    # Selection sort was faster than bubble sort. I think this is because bubble sort needs to iterate through the list every
    # time to make sure no more swaps need to be made. Whereas with selection sort, the lowest value being moved to the front
    # means that after getting to the end of the list, there won't be a value lower than what is currently at the start.

main()