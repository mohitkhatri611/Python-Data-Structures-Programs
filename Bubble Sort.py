def bs(a):
    b=len(a)-1
    for x in range(b):
        for y in range(b-x):
            if a[y] > a[y+1]:
                a[y], a[y+1] = a[y+1], a[y] # Observe the way of swapping  New.

    return a

a=[3,6,1,8]
bs(a)
print(a)

"""
#other way of doing
def sort(nums):

    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp


nums = [5, 3, 8, 6, 7, 2]
sort(nums)

print(nums)

"""