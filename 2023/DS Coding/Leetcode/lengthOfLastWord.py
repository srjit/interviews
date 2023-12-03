

def lengthOfLastWord(s: str) -> int:

    _s = list(s)
    for i  in range(len(_s)-1, -1 , -1):
        #import ipdb; ipdb.set_trace()
        if _s[i] != " ":
            count = 0
            while i > -1 and _s[i] != " ":
                count +=1
                i -= 1
            return count
        

print(lengthOfLastWord("a"))