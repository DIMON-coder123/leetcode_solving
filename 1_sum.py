nums = [3, 2, 4]
target = 6

h = {}

for i in range(len(nums)):
    h[nums[i]] = i

for i in range(len(nums)):
     diff = target - nums[i]
     if diff in h.keys() and h[diff] != i:
         print(i, nums.index(diff))



