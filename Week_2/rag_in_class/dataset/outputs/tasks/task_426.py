def filter_oddnumbers(nums):
    """Filter and return a list of odd numbers from the input list."""
    odd_nums = list(filter(lambda x: x % 2 != 0, nums))
    return odd_nums
