class Solution:  
    def subtractProductAndSum(self, n):
        sum, mum = 0,1
        for i in list(map(int,str(n))):
            sum+=int(i)
            mum*=int(i)
        return mum-sum