def generateParenthesis():
    
    def generatepar(n):
        if n == 1: 
            return ['()']
        elif n == 0:
            return ['']
        else:
            tmp = generatepar(n-1)
            result = []
            for i in range(len(tmp)):
                tmp_element_1 = '(' + tmp[i] + ')'
                tmp_element_2 = '()' + tmp[i]
                tmp_element_3 = tmp[i] + '()'
                if tmp_element_1 not in result:
                    result.append(tmp_element_1)
                if tmp_element_2 not in result:
                    result.append(tmp_element_2)
                if tmp_element_3 not in result:
                    result.append(tmp_element_3)

            tmp_n_2 = generatepar(n-2)
            for i in range(len(tmp_n_2)):
                tmp_element_1 = tmp_n_2[i] + '(())'
                tmp_element_2 = '(())' + tmp_n_2[i]
                if tmp_element_1 not in result:
                    result.append(tmp_element_1)
                if tmp_element_2 not in result:
                    result.append(tmp_element_2)

            return result
    return generatepar

def generateParenthesis(n):
    result = []
    stack = []
    stack.append(('',n,n))
    
    while stack:
        sofar, left, right = stack.pop()
        if left == 0 and right == 0:
            result.append(sofar)
        if left > 0:
            stack.append((sofar + "(",left-1, right))
        if right > left:
            stack.append((sofar + ")", left, right-1))
    return result  


print(generateParenthesis(3))


        