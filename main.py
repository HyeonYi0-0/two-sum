def twoSum(nums, target) :
  listLength = len(nums)
  res = []
  for i in range(listLength-1) :
    for j in range(i+1, listLength) :
      if((nums[i] + nums[j]) == target) :
        res.append(i)
        res.append(j)
    
  return res

print("input: ", end="")
nums = list(map(int, input().split()))

target = int(input("target: "))

print(twoSum(nums, target))