import time

nemo = ["nemo"]

def findNemo(array):
    time_start = time.time()
    for i in range(len(array)):
        if array[i] == "nemo":
            print("Found a NEMO!")
    time_end = time.time()
    print("Time:", time_end - time_start)

findNemo(nemo)