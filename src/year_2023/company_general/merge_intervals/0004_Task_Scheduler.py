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
from collections import deque
from typing import List

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s]: %(message)s",
)
logger.setLevel(logging.INFO)


class SolutionInTheWorks:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        Given a characters array tasks, representing the tasks a CPU needs
        to do, where each letter represents a different task. Tasks could
        be done in any order. Each task is done in one unit of time. For
        each unit of time, the CPU could complete either one task or just
        be idle.

        However, there is a non-negative integer n that represents the
        cooldown period between two same tasks (the same letter in the array),
        that is that there must be at least n units of time between any
        two same tasks.

        Return the least number of units of times that the CPU will take to
        finish all the given tasks.

        Parameters
        --------------

        Returns
        --------------


        Links
        --------------
        https://leetcode.com/problems/task-scheduler/


        Raises
        --------------
        """
        # Define the output of possible units of time needed to complete
        # all the tasks
        n_cpu_units = 0

        # Get frequencies of tasks
        task_frequency = {}
        for elem in tasks:
            task_frequency[elem] = 1 + task_frequency.get(elem, 0)

        # Determining the order of the keys when sorting based on counts
        # NOTE: The order of these are now in descending order
        task_sorted_by_frequency = [
            k
            for k, _ in sorted(
                task_frequency.items(),
                key=lambda x: x[1],
                reverse=True,
            )
        ]

        # Start populating array and keeping track of the index of
        # last seen for the given task
        last_seen = {}
        n_elem_left = sum(task_frequency.values())
        task_order = []

        while n_elem_left > 0:
            # Loop over the specified tasks in descending order
            for task_id in task_sorted_by_frequency:
                if task_frequency[task_id] == 0:
                    continue

                # Decreasing the number in the frequency hashmap
                task_frequency[task_id] -= 1
                n_elem_left -= 1

                # Checking then the letter was last seen
                last_seen[task_id] = last_seen.get(task_id, 0) + n_cpu_units

                while (n_cpu_units - last_seen[task_id]) < n:
                    n_cpu_units += 1
                    task_order.append("EMPTY")

                # Removing task frequency
                task_order.append(task_id)

                # Increasing count
                n_cpu_units += 1

        return n_cpu_units


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        Given a characters array tasks, representing the tasks a CPU needs
        to do, where each letter represents a different task. Tasks could
        be done in any order. Each task is done in one unit of time. For
        each unit of time, the CPU could complete either one task or just
        be idle.

        However, there is a non-negative integer n that represents the
        cooldown period between two same tasks (the same letter in the array),
        that is that there must be at least n units of time between any
        two same tasks.

        Return the least number of units of times that the CPU will take to
        finish all the given tasks.

        Parameters
        --------------

        Returns
        --------------


        Links
        --------------
        https://leetcode.com/problems/task-scheduler/


        Raises
        --------------
        """

        # --- Count frequencies of each tasks
        freq = {}
        for task in tasks:
            freq[task] = 1 + freq.get(task, 0)

        # --- Initialize variables
        # Units of time
        time = 0
        # Queue
        queue = deque()  # [-ct , idle tile]
        # Heap
        maxHeap = [-ct for ct in freq.values()]
        heapq.heapify(maxHeap)

        # --- Iterating over the tasks
        while maxHeap or queue:
            print(
                f"Before | time: {time} | maxHeap: {maxHeap} | queue: {queue}"
            )
            # Increasing unit of time
            time += 1

            if maxHeap:
                # We want to process the next task
                # NOTE: Adding a '1' since we want to bring the count to zero.
                ct = 1 + heapq.heappop(maxHeap)

                if ct:
                    # Add it to the queue
                    queue.append([ct, time + n])

            if queue and queue[0][1] == time:
                # Take it from the queue and insert it into the maxHeap
                heapq.heappush(maxHeap, queue.popleft()[0])

            print(
                f"After  | time: {time} | maxHeap: {maxHeap} | queue: {queue}\n"  # noqa: E501
            )

        return


if __name__ == "__main__":
    # Input parameters
    tasks = ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G", "B"]
    n = 2
    # Instantiating object
    # a = SolutionInTheWorks().leastInterval(tasks=tasks, n=n)
    a = Solution().leastInterval(tasks=tasks, n=n)
    # Printing out solution
    logger.info(f"Solution: {a}")
