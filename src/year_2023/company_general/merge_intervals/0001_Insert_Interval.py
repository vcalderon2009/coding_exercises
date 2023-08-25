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
    def insert(
        self,
        intervals: List[List[int]],
        newInterval: List[int],
    ) -> List[List[int]]:
        """
        You are given an array of non-overlapping intervals intervals
        where intervals[i] = [starti, endi] represent the start and the
        end of the ith interval and intervals is sorted in ascending order
        by starti. You are also given an interval newInterval = [start, end]
        that represents the start and end of another interval.

        Insert newInterval into intervals such that intervals is still
        sorted in ascending order by starti and intervals still does not
        have any overlapping intervals (merge overlapping intervals
        if necessary).

        Return intervals after the insertion.

        Parameters
        --------------


        Returns
        --------------


        Links
        --------------
        https://leetcode.com/problems/insert-interval/


        Raises
        --------------
        """
        # Initialize output variable
        output = []

        # Iterating over intervals
        for idx in range(len(intervals)):
            current_interval = intervals[idx]

            # If the 'newInterval' occurs before the current interval
            if newInterval[1] < current_interval[0]:
                # Adding the new interval to the output array
                output.append(newInterval)
                return output + intervals[idx:]
            elif current_interval[1] < newInterval[0]:
                # The interval occurs after the current interval, so we
                # only need to add the current interval
                output.append(current_interval)
            else:
                # The two interval overal, so we merge them.
                newInterval = [
                    min(newInterval[0], current_interval[0]),
                    max(newInterval[1], current_interval[1]),
                ]

        # For example, if the set of intervals is empty, then we just add
        # the new interval to the output array
        output.append(newInterval)

        return output


if __name__ == "__main__":
    # Input parameters
    intervals = [[1, 2], [3, 4], [5, 8], [9, 15]], [2, 5]
    newInterval = [4, 8]
    # intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    # newInterval = [4, 8]

    # Instantiating object
    a = Solution().insert(intervals=intervals, newInterval=newInterval)
    # Printing out solution
    logger.info(f"a: {a}")
