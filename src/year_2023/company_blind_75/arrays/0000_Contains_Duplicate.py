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
    def test_function(self, nums: List) -> None:
        """
        Given an integer array nums, return true if any value appears at
        least twice in the array, and return false if every element is
        distinct.

        Parameters
        --------------
        nums : list
            List containing set of numbers.

        Returns
        --------------
        duplicates : bool
            If ``True``, ``nums`` contains`` duplicates. Otherwise,
            there are no duplicates in ``nums``.

        Links
        --------------
        https://leetcode.com/problems/contains-duplicate/


        Raises
        --------------
        """
        return (
            False
            if (not nums or len(nums) == 1)
            else len(set(nums)) != len(nums)
        )


if __name__ == "__main__":
    # Input parameters
    nums = [1, 2, 3, 4]
    # Instantiating object
    a = Solution().test_function(nums)
    # Printing out solution
    logger.info(f"nums: {nums}")
    logger.info(f"a: {a}")
