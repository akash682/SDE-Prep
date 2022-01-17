def maximumUnits(boxTypes, truckSize):
    sorted_boxtypes = sorted(boxTypes,key=lambda a: a[1], reverse=True)
    sumunit = 0
    remain = truckSize
    for i in range(len(sorted_boxtypes)): 
        if remain == 0:
            break
        elif remain >= sorted_boxtypes[i][0]:
            sumunit += sorted_boxtypes[i][0]*sorted_boxtypes[i][1]
            remain = remain - sorted_boxtypes[i][0]
        elif remain < sorted_boxtypes[i][0]:
            sumunit += remain*sorted_boxtypes[i][1]
            remain = 0
    return sumunit

boxTypes = [[5,10],[2,5],[4,7],[3,9]]
truckSize = 10

print(maximumUnits(boxTypes,truckSize))