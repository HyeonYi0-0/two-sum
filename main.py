def twoSum(nums: list[int], target: int) -> list[int] :
  listLength = len(nums)
  res = []
  for i in range(listLength-1) :
    for j in range(i+1, listLength) :
      if((nums[i] + nums[j]) == target) :
        res.append(i)
        res.append(j)
    
  return res