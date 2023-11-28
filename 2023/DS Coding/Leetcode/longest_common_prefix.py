import numpy as np
from typing import List


def longestCommonPrefix(v: List[str]) -> str:
        ans=""
        v=sorted(v)
        first=v[0]
        last=v[-1]
        print(f"First: {first}, Last {last}")
        for i in range(min(len(first),len(last))):
            if(first[i]!=last[i]):
                return ans
            ans+=first[i]
        return ans 

print(longestCommonPrefix(["flow", "flower","fleece","flute"]))
#print(longestCommonPrefix(["a"]))