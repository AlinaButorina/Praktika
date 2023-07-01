def find_permutations(nums):
    if len(nums) == 0:
        return [[]]
    elif len(nums) == 1:
        return [nums]
    else:
        permutations = []
        for i in range(len(nums)):
            m = nums[i]
            remain_nums = nums[:i] + nums[i + 1:]
            for p in find_permutations(remain_nums):
                permutations.append([m] + p)
        return permutations


numbers = [1, 2, 3]
permutations = find_permutations(numbers)
print(permutations)
