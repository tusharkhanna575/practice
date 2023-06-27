def moveZeros(nums):
    k=0
    for i in range(len(nums)):
        if(nums[i]!=0):
            nums[i],nums[k]=nums[k],nums[i]
            k+=1

nums=list(map(int,input("Enter the array elements : ").split()))
moveZeros(nums)
print("Resultant array is : ", nums)