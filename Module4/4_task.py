def find_combinations(nums, target):
    result = []
    nums.sort()
    backtrack(nums, target, [], result)
    return result


def backtrack(nums, target, path, result):
    if target < 0:
        return
    if target == 0:
        result.append(path)
        return
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        backtrack(nums[i + 1:], target - nums[i], path + [nums[i]], result)


numbers = [2, 5, 2, 1, 2]
target_sum = 5

unique_combinations = find_combinations(numbers, target_sum)
print(unique_combinations)
