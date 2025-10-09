# def maxFrequencyElements(self,nums):
#     _n = []
#     _tes = nums[:].__len__()
#     for index in range(0, nums.__len__()):
#         _n.append(nums.count(nums[0]))
#         nums.remove(nums[0])
#     max_n = max(_n)
#     t = _n.count(max_n)
#     if max_n == 1:
#         return _tes
#     elif t == 0:
#         return max_n
#     return max_n * t
#
#
# print(maxFrequencyElements([8, 2, 8, 6, 1, 1, 8]))
def isPalindrome(s):
    s = s.lower()
    filtered = ''.join(filter(str.isalnum, s.lower()))
    print(filtered)

    return filtered == filtered[::-1]


print(isPalindrome("  "))
