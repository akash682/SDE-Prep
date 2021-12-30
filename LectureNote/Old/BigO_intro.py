# Big O notation is the language we use for talking about how log an algorithm takes to run.
# It describes the scalability of the program, when the elements or arguments gets bigger and bigger how much it slows down, how quickly the runtime grouws


import time

nemo = ['nemo']
everyone = ['dory', 'bruce', 'marlin', 'nemo', 'gill', 'bloat']
large = ['nemo']*100000

def findNemo(array):
    #start = time.time()
    for i in range(len(array)):
        if array[i]== 'nemo':
            print('Found NEMO!')
    #end = time.time()
    #print(end - start)


findNemo(nemo) # O(n) Linear Time
findNemo(everyone)
findNemo(large)

def compressFirstBox(array):
    print(array[0])

def compressFirstBox2(array):
    print(array[0])
    print(array[1])

compressFirstBox(nemo) # O(1)
compressFirstBox(everyone) # O(2) but we just say O(1) 