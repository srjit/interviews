

values = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

import pdb

def romanToInt3(num: str) -> int:

       
    prev = values[num[0]]
    op = prev
    for s in num[1:]:
        val = values[s] 
        if val > prev:
            op -= prev
            val -= prev
        op += val
        prev = val
        
        
    return op
    




def romanToInt(s: str) -> int:
    
    # start  from left to right
    # create groups - each group stop where lower value comes next
    # sum up

    letters = list(s)
    digits = [values[x] for x in letters]

    groups = []
    group = [digits[0]]
    prev = digits[0]
    for digit in digits[1:]:

        if digit > prev:
            group.append(digit)
        else:
            groups.append(group)
            group = [digit]
        prev = digit
    groups.append(group)
    tosum = []
    for group in groups:
        if len(group) == 1:
            tosum.append(group[0])
        else:
            sub = group[-1]
            group.reverse()
            for num in group[1:]:
                sub -= num
            tosum.append(sub)
    return sum(tosum)

            



def romanToInt2(self, s: str) -> int:
        
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += translations[char]
        return number


print(romanToInt3("MCM"))
print(romanToInt3("MCMXCIV"))
print(romanToInt3("LVIII"))
print(romanToInt3("III"))