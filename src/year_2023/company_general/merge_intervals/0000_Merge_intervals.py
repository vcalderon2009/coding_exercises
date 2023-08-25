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
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Given an array of intervals where intervals[i] = [starti, endi],
        merge all overlapping intervals, and return an array of the
        non-overlapping intervals that cover all the intervals in the input.

        Parameters
        --------------
        intervals : list
            List of intervals representing the start and end time of
            meetings.


        Returns
        --------------


        Links
        --------------
        https://leetcode.com/problems/merge-intervals/


        Raises
        --------------
        """
        # Define the output list
        output = []

        # Sort intervals in ascending start time
        sorted_intervals = sorted(
            intervals,
            key=lambda x: x[0],
            reverse=False,
        )

        # Iterating over the intervals
        for idx in range(len(sorted_intervals)):
            meeting = sorted_intervals[idx]
            # Adding interval if it's the first iteration or if the
            # interval is outside the current range
            if not output or output[-1][-1] < meeting[0]:
                output.append(meeting)
            else:
                output[-1][-1] = max(output[-1][-1], meeting[1])

        return output


if __name__ == "__main__":
    # Input parameters
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    # Instantiating object
    a = Solution().merge(intervals=intervals)
    # Printing out solution
    logger.info(f"Output: {a}")
