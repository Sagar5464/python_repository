from functools import cmp_to_key
def compare(x, y):
    if x + y > y + x:
        return -1
    else:
        return 1
def largest_number(nums):
    nums = list(map(str, nums))
    nums.sort(key=cmp_to_key(compare))
    return ''.join(nums)
a = [54, 546, 548, 60]
print("The largest number formed is:", largest_number(a))
