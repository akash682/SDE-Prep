open_seen = []

def isvalidbracket(s):
    hash_bracket = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    for i in range(len(s)):
        if s[i] not in hash_bracket:
            open_seen.append(s[i])
        elif s[i] in hash_bracket:
            if open_seen.pop() != hash_bracket[s[i]]:
                return False
    if not open_seen:
        return True
    else:
        return False

print(isvalidbracket("((("))
print(open_seen)

print(isvalidbracket("((()))"))
print(open_seen)