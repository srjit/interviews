class Solution:
    
    
    def add_to_dict(self, c, dict_={}):
        
        stop = False
        if c not in dict_:
            dict_[c] = 1
        else:
            dict_[c] += 1
            stop = True
        return stop
            
    
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        longest = s[0]
        for i,c in enumerate(s):
            dict_ = {}
            subs = ""
            for c_ in s[i:]:
                stop = self.add_to_dict(c_, dict_)
                if stop:
                    if len(longest) < len(subs):
                        longest = subs
                    break
                else:
                    subs += c_

        return len(longest)
                
            
                
        
        
a = Solution()
# print(a.lengthOfLongestSubstring("abcabcbb"))
# print(a.lengthOfLongestSubstring("bbbbb"))
# print(a.lengthOfLongestSubstring("pwwkew"))
print(a.lengthOfLongestSubstring(" "))
        
