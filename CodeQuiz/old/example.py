lists = []
l = [5,1,6]
for i in range(len(l) + 1):
        for j in range(i):
            lists.append(l[j: i])

print(lists)