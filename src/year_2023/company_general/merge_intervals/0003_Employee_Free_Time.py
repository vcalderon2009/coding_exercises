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

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s]: %(message)s",
)
logger.setLevel(logging.INFO)


# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end


class Solution:
    def employeeFreeTime(self, schedule: "[[Interval]]") -> "[Interval]":
        """
        FUNCTION DESCRIPTION

        Parameters
        --------------

        Returns
        --------------


        Links
        --------------
        https://leetcode.com/problems/employee-free-time/


        Raises
        --------------

        Steps
        ----------
        1.  Combine all intervals and sort them based on 'start' time
        2.  Merge the corresponding intervals
        3.  Calculate the interval between the end time and start time
            of the intervals.
        """
        # Variable to keep track of the 'merged' intervals
        intervals = []

        #   1. Combine all intervals and sort them based on the start time
        for elem in schedule:
            intervals.extend(elem)

        #   Sorting them based on start time
        intervals.sort(key=lambda x: x.start)

        #   2. Merge the corresponding intervals
        merged_intervals = []

        for elem in intervals:
            if not merged_intervals or merged_intervals[-1].end < elem.start:
                merged_intervals.append(elem)
            else:
                merged_intervals[-1].end = max(
                    merged_intervals[-1].end, elem.end
                )

        #   Find the time between each intervals
        employee_free_time = []

        for ii in range(1, len(merged_intervals)):
            employee_free_time.append(
                Interval(
                    start=merged_intervals[ii - 1].end,
                    end=merged_intervals[ii].start,
                )
            )

        return employee_free_time


class Solution_alternative:
    def employeeFreeTime(self, schedule: "[[Interval]]") -> "[Interval]":
        """
        FUNCTION DESCRIPTION

        Parameters
        --------------

        Returns
        --------------


        Links
        --------------
        https://leetcode.com/problems/employee-free-time/


        Raises
        --------------

        Steps
        ----------
        1.  Combine all intervals and sort them based on 'start' time
        2.  Merge the corresponding intervals
        3.  Calculate the interval between the end time and start time
            of the intervals.
        """
        # 1.    Looping over each interval and only keeping track of the
        #       starting time
        free_time_intervals = []

        heap = [(schedule[ii][0].start, ii, 0) for ii in range(len(schedule))]
        # We now convert the array into a heap
        heapq.heapify(heap)

        # We now instantiate the variable to keep track of the previous time
        # NOTE: We basically choose the first element of the heap and
        # choose the 'start' time
        previous = schedule[heap[0][1]][heap[0][2]].start

        # Iterate over the heap value
        while heap:
            # Popping out the result from the heap
            _, schedule_idx, employee_interval_idx = heapq.heappop(heap)
            interval = schedule[schedule_idx][employee_interval_idx]

            # If there is a gap between 'previous' and the 'start' of
            # the current interval, that means this is a 'free' time slot.
            if previous < interval.start:
                free_time_intervals.append(
                    Interval(*(previous, interval.start))
                )

            # Now we have to update the 'previous' value to the max between
            # the 'previous' value and the 'end' time of the current interval
            previous = max(previous, interval.end)

            # If there is another interval for the SAME employee, then
            # add that to the heap
            if (employee_interval_idx + 1) < len(schedule[schedule_idx]):
                # Adding the interval to the heap
                heapq.heappush(
                    heap,
                    (
                        schedule[schedule_idx][
                            employee_interval_idx + 1
                        ].start,
                        schedule_idx,
                        employee_interval_idx + 1,
                    ),
                )

        return free_time_intervals


if __name__ == "__main__":
    # Input parameters
    schedule_raw = [[[1, 2], [5, 6]], [[1, 3]], [[4, 10]]]
    schedule = [[Interval(*xx) for xx in elem] for elem in schedule_raw]
    # Instantiating object
    # a = Solution().employeeFreeTime(schedule=schedule)
    a = Solution_alternative().employeeFreeTime(schedule=schedule)
    # Printing out solution
    logger.info(f"Solution: {a}")
