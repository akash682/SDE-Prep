def romanToInt(self, s: str) -> int:
    #Hash Map for Roman to Integer
    hash_ri = {
            'M' : 1000,
            'D' : 500,
            'C' : 100,
            'L' : 50,
            'X' : 10,
            'V' : 5,
            'I' : 1,
            'IV' : 4,
            'IX' : 9,
            'XL' : 40,
            'XC' : 90,
            'CD' : 400,
            'CM' : 900
    }
        

    sum = 0
    skip_flag = False
    # Loop through the string s
    for i in range(len(s)):
        if skip_flag:
            skip_flag = False
            continue
        else:
            if s[i:i+2] in hash_ri:
                sum += hash_ri[s[i:i+2]]
                skip_flag = True
            else:
                sum += hash_ri[s[i]]

    #Go backwards
    #Hash Map for Roman to Integer
    hash_ri = {
            'M' : 1000,
            'D' : 500,
            'C' : 100,
            'L' : 50,
            'X' : 10,
            'V' : 5,
            'I' : 1
    }
        

    sum = 0
    i = len(s) - 1
    prev = 0
    # Loop through the string s
    while True:
        if i < 0:
            break
        else:
            cur = hash_ri[s[i]]
            if cur < prev:
                sum -= cur
            else:
                sum += cur
            prev = cur
            i -= 1
        
    return sum   
            