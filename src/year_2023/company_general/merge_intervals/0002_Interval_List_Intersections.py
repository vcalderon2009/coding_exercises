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
    def intervalIntersection(
        self,
        firstList: List[List[int]],
        secondList: List[List[int]],
    ) -> List[List[int]]:
        """
        You are given two lists of closed intervals, firstList and secondList,
        where firstList[i] = [starti, endi] and secondList[j] = [startj, endj].
        Each list of intervals is pairwise disjoint and in sorted order.

        Return the intersection of these two interval lists.

        A closed interval [a, b] (with a <= b) denotes the set of real
        numbers x with a <= x <= b.

        The intersection of two closed intervals is a set of real numbers
        that are either empty or represented as a closed interval. For
        example, the intersection of [1, 3] and [2, 4] is [2, 3].

        Parameters
        --------------

        Returns
        --------------


        Links
        --------------
        https://leetcode.com/problems/interval-list-intersections/


        Raises
        --------------
        """
        # Checking edge cases
        if not firstList or not secondList:
            return []

        # Initialize pointers
        first, second = 0, 0
        output = []

        # Iterating over each interval
        while first < len(firstList) and second < len(secondList):
            # Defining elements
            first_interval = firstList[first]
            second_interval = secondList[second]

            # Checking whether or not the intervals intersect
            low = max(first_interval[0], second_interval[0])
            high = min(first_interval[1], second_interval[1])

            if low <= high:
                output.append([low, high])

            # Moving to the next interval based on which one finishes earlier
            if first_interval[1] < second_interval[1]:
                first += 1
            else:
                second += 1

        return output


if __name__ == "__main__":
    # Input parameters
    firstList = [[0, 2], [5, 10], [13, 23], [24, 25]]
    secondList = [[1, 5], [8, 12], [15, 24], [25, 26]]
    # Instantiating object
    a = Solution().intervalIntersection(
        firstList=firstList,
        secondList=secondList,
    )
    # Printing out solution
    logger.info(f"a: {a}")
