#---------------------------------------#
from collections import Counter as ct 
#---------------------------------------#

def rearrange_by_frequency(nums: list[int]) -> list[int]:
    C = ct(nums)
    return sorted(nums, key=lambda x : (-C[x], x))

print(rearrange_by_frequency([4, 5, 6, 5, 4, 3, 4]))
