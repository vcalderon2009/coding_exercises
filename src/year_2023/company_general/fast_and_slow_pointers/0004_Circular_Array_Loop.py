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
    def circularArrayLoop(self, nums: List[int]) -> bool:
        """
        You are playing a game involving a circular array of non-zero
        integers nums. Each nums[i] denotes the number of indices
        forward/backward you must move if you are located at index i:

            If nums[i] is positive, move nums[i] steps forward, and
            If nums[i] is negative, move nums[i] steps backward.

        Since the array is circular, you may assume that moving forward
        from the last element puts you on the first element, and moving
        backwards from the first element puts you on the last element.

        A cycle in the array consists of a sequence of indices seq of
        length k where:

            -   Following the movement rules above results in the repeating
                index sequence
                seq[0] -> seq[1] -> ... -> seq[k - 1] -> seq[0] -> ...
            -   Every nums[seq[j]] is either all positive or all negative.
            -   k > 1

        Return true if there is a cycle in nums, or false otherwise.

        Parameters
        --------------

        Returns
        --------------


        Links
        --------------
        https://leetcode.com/problems/circular-array-loop/


        Raises
        --------------

        Notes
        --------------
        """
        if len(nums) <= 1:
            return False

        # Length of array
        n_elem = len(nums)

        # Iterating over each number in array as 'starting' points
        for idx in range(len(nums)):
            # Defining slow and fast pointers at the element ``idx``
            slow = idx
            fast = idx

            # Determining the direction to move
            # NOTE: The direction matters since this will dictate if the
            # direction is 'forwards' or 'backwards'.
            forward_direction = nums[idx] > 0

            # Iterating until both pointers are the same
            while True:
                # Update both pointers
                slow = (slow + nums[slow]) % n_elem
                if slow < 0:
                    slow += n_elem
                if (nums[slow] > 0) != forward_direction:
                    break

                fast = (fast + nums[fast]) % n_elem
                if fast < 0:
                    fast += n_elem
                if (nums[fast] > 0) != forward_direction:
                    break
                # Doing it again for 'fast'
                fast = (fast + nums[fast]) % n_elem
                if fast < 0:
                    fast += n_elem
                if (nums[fast] > 0) != forward_direction:
                    break

                # Check if both pointers are the same
                if slow == fast:
                    return True

        return False


if __name__ == "__main__":
    # Input parameters
    nums = [2, -1, 1, 2, 2]
    # Instantiating object
    a = Solution().circularArrayLoop(nums=nums)
    # Printing out solution
    logger.info(f"a: {a}")
