def generate(numRows):
    """
    [1]
    [1,1]
    [1,1,1,1] --> [1,2,2,1]
    [1,1,2,2,1,1] --> [1,2,3,3,2,1]
    """
    res = []
        
    if numRows == 1:
        return [[1]]
    if numRows == 2:
        return [[1],[1,1]]
        
    stack = [[1],[1,1]]
        
    for i in range(numRows):
        prev_level = stack[-1]
        tmp = []
        for i in range(0, len(prev_level)-1):
            tmp.append(prev_level[i] + prev_level[i+1])
        first = [1]
        first.extend(tmp)
        first.append(1)
        stack.append(first)
    return stack

print(generate(5))