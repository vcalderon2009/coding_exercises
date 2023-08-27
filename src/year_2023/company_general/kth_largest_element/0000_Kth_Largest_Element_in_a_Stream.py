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
from typing import List

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s]: %(message)s",
)
logger.setLevel(logging.INFO)


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        """
        Design a class to find the kth largest element in a stream. Note
        that it is the kth largest element in the sorted order, not the kth
        distinct element.

        Implement KthLargest class:

            -   KthLargest(int k, int[] nums) Initializes the object with
                the integer k and the stream of integers nums.
            -   int add(int val) Appends the integer val to the stream and
            returns the element representing the kth largest element in
            the stream.

        Parameters
        --------------

        Returns
        --------------


        Links
        --------------
        https://leetcode.com/problems/kth-largest-element-in-a-stream/


        Raises
        --------------
        """
        # Initializing variables
        self.nums = nums
        self.k = k

        # Instantiating maxHeap, since we want to access the kth-largest
        # element in the array
        self.maxHeap = []

        for elem in nums:
            heapq.heappush(self.maxHeap, elem)

        # Removing values from the maxHeap, in order for the maxHeap to
        # only contain 'k' elements
        while len(self.maxHeap) > k:
            heapq.heappop(self.maxHeap)

    def add(self, val: int) -> int:
        # Updating the stream
        self.nums.append(val)

        # Pushing the value to the heap
        heapq.heappush(self.maxHeap, val)

        if len(self.maxHeap) > self.k:
            heapq.heappop(self.maxHeap)

        return self.maxHeap[0]


if __name__ == "__main__":
    # Input parameters
    # Instantiating object
    kthLargest = KthLargest(k=3, nums=[4, 5, 8, 2])
    kthLargest.add(val=3)
    kthLargest.add(5)
    kthLargest.add(10)
    kthLargest.add(9)
    kthLargest.add(4)
    # Printing out solution
    logger.info(f"Solution: {kthLargest}")
