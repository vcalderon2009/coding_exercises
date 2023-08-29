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
from collections import defaultdict
from typing import List

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s]: %(message)s",
)
logger.setLevel(logging.INFO)


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        You are given a network of n nodes, labeled from 1 to n. You are
        also given times, a list of travel times as directed edges
        times[i] = (ui, vi, wi), where ui is the source node, vi is the
        target node, and wi is the time it takes for a signal to travel from
        source to target.

        We will send a signal from a given node k. Return the minimum time
        it takes for all the n nodes to receive the signal. If it is
        impossible for all the n nodes to receive the signal, return -1.

        Parameters
        --------------

        Returns
        --------------


        Links
        --------------
        https://leetcode.com/problems/network-delay-time/


        Raises
        --------------
        """
        # Creating dictionary to store information about each node and
        # each of its edges.
        nodes_dict = defaultdict(list)
        for elem in times:
            source, receiver, time_delay = elem
            nodes_dict[source].append((time_delay, receiver))

        # Initialize
        delay_time = 0
        visited = set()
        # Initializing the heap with the source node and the time of '0'
        minHeap = [(0, k)]

        while minHeap:
            # Extracting the node from the minHeap
            time, node = heapq.heappop(minHeap)

            if node in visited:
                continue

            # Adding node to visited set
            visited.add(node)

            # Comparing the delay time and the current time
            delay_time = max(delay_time, time)

            # Exploring the neighbors, if any, and adding them to the
            # minHeap
            if node in nodes_dict:
                for neighbour_delay, neighbour_node in nodes_dict.get(node):
                    # Adding each neighbor to the minHeap
                    heapq.heappush(
                        minHeap,
                        (time + neighbour_delay, neighbour_node),
                    )

        return delay_time if len(visited) == n else -1


if __name__ == "__main__":
    # Input parameters
    times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    n = 4
    k = 2
    # Instantiating object
    a = Solution().networkDelayTime(times=times, n=n, k=k)
    # Printing out solution
    logger.info(f"Solution: {a}")
