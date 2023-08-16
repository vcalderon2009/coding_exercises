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
    def test_function(self, nums: List[int], target: int) -> None:
        """
        FUNCTION DESCRIPTION

        Parameters
        --------------
        Given an array of integers nums and an integer target, return indices
        of the two numbers such that they add up to target.

        You may assume that each input would have exactly one solution,
        and you may not use the same element twice.

        You can return the answer in any order.

        Returns
        --------------


        Links
        --------------
        https://leetcode.com/problems/two-sum/


        Raises
        --------------
        """
        # Create set of values with indices
        idx_dict = {xx: idx for idx, xx in enumerate(nums)}
        # Looping over each element
        for idx, elem in enumerate(nums):
            complement = target - elem
            if (complement in idx_dict) and (idx != idx_dict[complement]):
                return [idx, idx_dict[complement]]

        return []


if __name__ == "__main__":
    # Input parameters
    nums = [2, 7, 11, 15]
    target = 9
    # Instantiating object
    a = Solution().test_function(nums, target)
    # Printing out solution
    logger.info(f"nums: {nums}")
    logger.info(f"target: {target}")
    logger.info(f"a: {a}")
