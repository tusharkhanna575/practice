def evenList(nums):
    ans=[x for x in nums if x%2==0]
    return ans

nums=list(map(int,input("Enter the array elements : ").split()))
ans=evenList(nums)
print("Resultant list is : ", ans)