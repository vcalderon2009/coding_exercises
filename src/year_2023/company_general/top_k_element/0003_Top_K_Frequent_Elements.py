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
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Given an integer array nums and an integer k, return the k most
        frequent elements. You may return the answer in any order.

        Parameters
        --------------

        Returns
        --------------


        Links
        --------------
        https://leetcode.com/problems/top-k-frequent-elements/


        Raises
        --------------
        """
        # Calculate the frequencies of each element in `nums`
        freq = {}
        for elem in nums:
            freq[elem] = 1 + freq.get(elem, 0)

        # Define the min Heap and only allow it to have 'k' elements
        minHeap = []

        for key, val in freq.items():
            # Adding value to the minHeap
            heapq.heappush(minHeap, (val, key))

            while len(minHeap) > k:
                heapq.heappop(minHeap)

        # Return the set of elements with the largest frequencies.
        output = [xx[1] for xx in minHeap]

        return output


if __name__ == "__main__":
    # Input parameters
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    # Instantiating object
    a = Solution().topKFrequent(nums=nums, k=k)
    # Printing out solution
    logger.info(f"Solution: {a}")
