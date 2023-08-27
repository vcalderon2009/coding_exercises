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


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Given an array of points where points[i] = [xi, yi] represents a
        point on the X-Y plane and an integer k, return the k closest points
        to the origin (0, 0).

        The distance between two points on the X-Y plane is the Euclidean
        distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

        You may return the answer in any order. The answer is guaranteed
        to be unique (except for the order that it is in).

        Parameters
        --------------

        Returns
        --------------


        Links
        --------------
        https://leetcode.com/problems/k-closest-points-to-origin/


        Steps
        --------------
        1.  Initialize a min heap
        2.  Push the elements one by one. Once the minHeap has reached
            'k' values, add the element and push the last element
        3.  Once all the elements have been passed through the min heap
            return the coordinates of the minHeap
        """
        dist_maxHeap = []

        for coords in points:
            # Adding coordinate to the maxHeap
            dist = coords[0] * coords[0] + coords[1] * coords[1]
            heapq.heappush(dist_maxHeap, (-dist, coords))

            while len(dist_maxHeap) > k:
                heapq.heappop(dist_maxHeap)

        return [xx[1] for xx in dist_maxHeap]


if __name__ == "__main__":
    # Input parameters
    points = [[3, 3], [5, -1], [-2, 4]]
    k = 2
    # Instantiating object
    a = Solution().kClosest(points=points, k=k)
    # Printing out solution
    logger.info(f"Solution: {a}")
