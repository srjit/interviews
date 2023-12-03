

class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[-1]*(n+2)
        def solve(i):
            if i==0 or i==1:
                return 1
            if dp[i]!=-1:
                return dp[i]
            left=solve(i-1)
            right=solve(i-2)
            dp[i]=left+right
            return left+right
        return solve(n)
    


def climbStairs(n: int) -> int:
    one,two=1,1
    for _ in range(n-1):
        one, two = two, one + two
    return two
    

print(climbStairs(2))