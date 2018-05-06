def groupSum(start, nums, target):
    if start == len(nums) - 1:
        return nums[start] == target
    return groupSum(start + 1, nums, target - nums[start]) or groupSum(start + 1, nums, target)#两种可能：使用这个位置的数或不使用
#print(groupSum(0, [2, 4, 8], 9))
def groupSum6(start, nums, target):
    if start == len(nums) - 1:
        return nums[start] == target
    if nums == 6:
        return groupSum6(start + 1, nums, target - nums[start])#必须使用6
    else:
        return groupSum6(start + 1, nums, target) or groupSum6(start + 1, nums, target - nums[start])#先测试不使用的再试使用的，保证先测出6
##print(groupSum6(0, [5, 2, 4, 6], 9))
def groupNoAdj(start, nums, target):
    if start >= len(nums):
        return target == 0
    return (groupNoAdj(start + 1, nums, target) or#不使用这个数的情况
        groupNoAdj(start + 2, nums, target - nums[start]))#使用这个数的情况
##print(groupNoAdj(0, [5, 10, 4, 1], 11))
def groupSum5(start, nums, target):
    if start >= len(nums) - 1:return target == 0
    if not nums[start] % 5:#是5的倍数，必须被选上
        if nums[start + 1] == 1:#5的倍数后是1，则1不能被选上
            return groupSum5(start + 2, nums, target - nums[start])
        return groupSum5(start + 1, nums, target - nums[start])
    return groupSum5(start + 1, nums, target) or groupSum5(start + 1, nums, target - nums[start])
##print(groupSum5(0, [3, 5, 1], 9))
def groupSumClump(start, nums, target):
    nlen = len(nums)
    if start >= nlen:return target == 0
    i = start
    value = 0#这个数值相同的块的总值
    while i < nlen and nums[i] == nums[start]:
        value += nums[start]
        i += 1
    #此时i是块最后一个数值的下一个的索引
    return groupSumClump(i, nums, target) or groupSumClump(i, nums, target - value)
##print(groupSumClump(0, [8, 2, 2, 1], 11))
