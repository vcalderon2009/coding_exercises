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

import logging
from collections import deque
from typing import List

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s]: %(message)s",
)
logger.setLevel(logging.INFO)


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        You are given an array of integers nums, there is a sliding window
        of size k which is moving from the very left of the array to the
        very right. You can only see the k numbers in the window.
        Each time the sliding window moves right by one position.

        Return the max sliding window.

        Parameters
        --------------

        Returns
        --------------


        Links
        --------------
        https://leetcode.com/problems/sliding-window-maximum/


        Raises
        --------------
        """
        # Initialize pointers
        left, right = 0, 0

        # Initialize queue and output array
        result = []
        queue = deque()

        # Iterating over the input array
        while right < len(nums):
            # We must first remove any value that is smaller than 'right'
            while queue and (queue[right] < nums[right]):
                queue.pop()
            # Append the right-most index to the queue
            queue.append(right)

            # Comparing the 'left' pointer to the first element in 'queue'
            if left > queue[0]:
                queue.popleft()

            # Only adding the value to the 'result'
            if (right + 1) >= k:
                result.append(nums[queue[0]])

        return result


if __name__ == "__main__":
    # Input parameters
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    # Instantiating object
    a = Solution().maxSlidingWindow(nums=nums, k=k)
    # Printing out solution
    logger.info(f"a: {a}")
