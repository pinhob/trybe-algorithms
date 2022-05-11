def find_duplicate(nums):
    if len(nums) <= 1:
        return False

    for num in nums:
        if not isinstance(num, int) or num < 1:
            return False

        num_duplicate_counter = nums.count(num)

        if num_duplicate_counter > 1:
            return num

    return False
