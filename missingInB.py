class Solution:
    def findMissing(self,a,b):
        b=set(b)
        miss=[]
        for i in a:
            if i not in b:
                miss.append(i)
        return miss
a=list(map(int,input().split()))
b=list(map(int,input().split()))
ob=Solution()
ans=ob.findMissing(a,b)
print("The elements not present in B are:")
for num in ans:
    print(num,end=" ")