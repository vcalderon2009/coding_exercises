#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# MIT License
#
# Copyright (c) 2023 Victor Calderon
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import heapq
import logging
from typing import List

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s]: %(message)s",
)
logger.setLevel(logging.INFO)


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Given an integer array nums and an integer k, return the kth
        largest element in the array.

        Note that it is the kth largest element in the sorted order, not
        the kth distinct element.

        Can you solve it without sorting?

        Parameters
        --------------

        Returns
        --------------


        Links
        --------------
        https://leetcode.com/problems/kth-largest-element-in-an-array/


        Raises
        --------------
        """
        if not nums:
            return

        # Create a minHeap
        minHeap = []

        for elem in nums:
            heapq.heappush(minHeap, elem)

            while len(minHeap) > k:
                heapq.heappop(minHeap)

        return minHeap[0]


if __name__ == "__main__":
    # Input parameters
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    # Instantiating object
    a = Solution().findKthLargest(nums=nums, k=k)
    # Printing out solution
    logger.info(f"Solution: {a}")
