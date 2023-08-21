""" 347. Top K Frequent Elements
    Author: Artur Gasparyan
    Date: 21 Aug 2023
    Link: https://leetcode.com/problems/top-k-frequent-elements/submissions/1027616833/
"""


from collections import Counter
import heapq


class Solution:
    @staticmethod
    def topKFrequent(nums, k):
        counts = Counter(nums)

        heap_nums = []
        for num, count in counts.items():
            heapq.heappush(heap_nums, (-count, num))

        ret_list = []
        while len(ret_list) < k:
            count, num = heapq.heappop(heap_nums)
            ret_list.append(num)

        return ret_list
