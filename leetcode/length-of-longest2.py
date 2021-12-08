

class Solution:


    def lengthOfLongest(self, s: str) -> int:

        chars = list(s)
        counts = []
        d_ = {}
        
        for i, c in enumerate(s):

            if c in d_:
                d_[c] = d_[c] + 1
                counts.append(str(d_[c]))

            else:
                d_[c] = 1
                counts.append("1")


        for i in range(len(counts)):
            if counts[i] != "1":
                counts[i] = "0"

        counts = "".join(counts)
        print(counts)
        longest_start_index = []
        for i in range(len(counts)):
            tmp = counts[i:]
            if i == len(counts)-1:
                longest_start_index.append(1)
            elif "0" in tmp and "0" != tmp[0]:
                longest_start_index.append(tmp.index("0") - i)
            elif "0" in tmp and "0" == tmp[0]:
                longest_start_index.append(tmp[1:].index("0") - i + 1)
            else:
                longest_start_index.append(len(tmp) - i)

        print(longest_start_index)
        return max(longest_start_index)
            

a = Solution()        
# print(a.lengthOfLongest("abcabcbb"))
print(a.lengthOfLongest("bbbb"))
print(a.lengthOfLongest("pwwkew"))
            
            
        
