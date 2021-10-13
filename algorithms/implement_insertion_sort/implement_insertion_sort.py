def insertion_sort(nums: list[float]) -> list[float]:
    for start in range(1, len(nums)):
        index = start

        while nums[index] < nums[index - 1] and index > 0:
            nums[index], nums[index - 1] = nums[index - 1], nums[index]
            index -= 1

    return nums
