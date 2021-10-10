"""
This Bubble Sort implementation uses a flag to terminate iterations early if
the list is already sorted, and uses a while loop instad of a for loop for
the outer iterations.

Because we don't know the outer iteration number, we need to iterate the
whole list (both unsorted and unsorted portions) on each inner loop.
"""


def bubble_sort(nums: list[float]) -> list[float]:
    is_sorted = False

    while (not is_sorted):
        is_sorted = True
        for index in range(len(nums) - 1):
            if nums[index] > nums[index + 1]:
                nums[index], nums[index + 1] = nums[index + 1], nums[index]
                is_sorted = False

    return nums
