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


class Solution:
    def reorganizeString(self, s: str) -> str:
        """
        Given a string s, rearrange the characters of s so that any two
        adjacent characters are not the same.

        Return any possible rearrangement of s or return "" if not possible.

        Parameters
        --------------

        Returns
        --------------


        Links
        --------------
        https://leetcode.com/problems/reorganize-string/


        Steps
        --------------
        1.  Calculate the frequency of each letter.
        2.  Construct a max heap (largest value at the bottom) with the
            frequencies and the corresponding letters of the string.
        3.  Iterate over the heap. Each time, pop the result and decrease
            the frequency of the letter.
        4.  Insert the again the letter and its corresponding decreased
            frequency.
        5.  Do it until there are no more available elements in the heap.
        """
        # --- Edge cases
        # String is empty
        if not s:
            return ""

        # Converting string to list and removing empty spaces
        s = [xx for xx in list(s) if xx != " "]

        # Calculating frequencies
        freq = {}
        for elem in s:
            freq[elem] = 1 + freq.get(elem, 0)

        # Define the 'max' Heap
        maxHeap = [(-val, letter) for letter, val in freq.items()]
        heapq.heapify(maxHeap)

        # --- Iterating over heap
        output = []
        previous = None

        while maxHeap or previous:
            # Returning an empty string, if applicable
            if previous and not maxHeap:
                return ""

            # Removing letter with maximum frequency
            letter_frequency, letter = heapq.heappop(maxHeap)

            # Decreasing the letter frequency and re-inserting it into heap
            letter_frequency += 1

            # Adding to the output
            output.append(letter)
            print(f"output: {output}")

            # Pushing letter to heap
            if previous:
                heapq.heappush(maxHeap, previous)
                previous = None

            # Saving count to variable
            if letter_frequency != 0:
                previous = (letter_frequency, letter)

        return "".join(output)


if __name__ == "__main__":
    # Input parameters
    s = "aabca"
    # Instantiating object
    a = Solution().reorganizeString(s=s)
    # Printing out solution
    logger.info(f"Solution: {a}")
