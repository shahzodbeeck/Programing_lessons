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
# def isPalindrome(s):
#     s = s.lower()
#     filtered = ''.join(filter(str.isalnum, s.lower()))
#     print(filtered)
#
#     return filtered == filtered[::-1]
#
#
# print(isPalindrome("  "))
# def findContentChildren(g, s) -> int:
#     children = 0
#     g_sorted = g
#     s_sorted = sorted(s)
#
#     i = 0
#     j = 0
#     while i < len(g_sorted) and j < len(s_sorted):
#         if s_sorted[j] >= g_sorted[i]:
#             children += 1
#             i += 1
#             j += 1
#         else:
#             j += 1
#     return children
# print(findContentChildren([10,9,8,7], [5,6,7,8]))

# def matchPlayersAndTrainers( players, trainers):
#     players.sort()
#     trainers.sort()
#     i = 0
#     j = 0
#     matches = 0
#     while i < len(players) and j < len(trainers):
#         if players[i] <= trainers[j]:
#             matches += 1
#             i += 1
#             j += 1
#         else:
#             j += 1
#     return matches
# print(matchPlayersAndTrainers([1,1,1], [10]))
def findMaxK( nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums_set = set(nums)
    max_k = -1
    for num in nums_set:
        if -num in nums_set:
            max_k = max(max_k, abs(num))
    return max_k

