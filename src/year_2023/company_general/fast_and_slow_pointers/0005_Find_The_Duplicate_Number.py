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
from typing import List

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s]: %(message)s",
)
logger.setLevel(logging.INFO)


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Given an array of integers nums containing n + 1 integers where each
        integer is in the range [1, n] inclusive.

        There is only one repeated number in nums, return this repeated number.

        You must solve the problem without modifying the array nums and uses
        only constant extra space.

        Parameters
        --------------
        nums : list
            List of integers of 1 <= n

        Returns
        --------------
        repeated_number : int
            Repeated number in ``num``.


        Links
        --------------
        https://leetcode.com/problems/find-the-duplicate-number/


        Raises
        --------------
        """

        def get_next_position(nums, idx) -> int:
            """
            Function to get the next value to use when iterating over ``nums``.
            """

            return nums[idx]

        # Initialize pointers
        slow = fast = 0

        # --- Step 1 - Find intersection
        while True:
            # Increasing pointers
            logger.info(f"Before | slow: {slow} | fast: {fast}")
            slow = get_next_position(nums=nums, idx=slow)
            fast = get_next_position(
                nums=nums,
                idx=get_next_position(
                    nums=nums,
                    idx=fast,
                ),
            )
            logger.info(f"After  | slow: {slow} | fast: {fast}\n\n")

            # Stop if both pointers are the same
            if slow == fast:
                break

        # -- Step 2 - Find point of entry, i.e. duplicate number in ``nums``.
        # Initialize 'slow' pointer again
        slow = 0

        while True:
            # Increasing pointers
            logger.info(f"Before 2 | slow: {slow} | fast: {fast}")
            slow = get_next_position(nums=nums, idx=slow)
            fast = get_next_position(nums=nums, idx=fast)
            logger.info(f"After 2  | slow: {slow} | fast: {fast}\n\n")

            if slow == fast:
                return slow


if __name__ == "__main__":
    # Input parameters
    nums = [2, 5, 8, 6, 8, 3, 9, 8, 1, 7]
    # Instantiating object
    a = Solution().findDuplicate(nums=nums)
    # Printing out solution
    logger.info(f"output: {a}")
