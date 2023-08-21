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
    def findRepeatedDnaSequences(self, s: str, k=int) -> List[str]:
        """
        The DNA sequence is composed of a series of nucleotides abbreviated
        as 'A', 'C', 'G', and 'T'.

            -   For example, "ACGAATTCCG" is a DNA sequence.

        When studying DNA, it is useful to identify repeated sequences
        within the DNA.

        Given a string s that represents a DNA sequence, return all the
        10-letter-long sequences (substrings) that occur more than once
        in a DNA molecule. You may return the answer in any order.

        Parameters
        --------------

        Returns
        --------------


        Links
        --------------
        https://leetcode.com/problems/repeated-dna-sequences/


        Raises
        --------------
        """
        # Initialize output array
        seen, output = set(), set()

        for left in range(len(s) - k + 1):
            substring = s[left : left + k]  # noqa: E203
            # If the substring has already been seen before.
            if substring in seen:
                # Adding it to the output set
                output.add(substring)
            # Adding substring to the 'seen' set
            seen.add(substring)

        return list(output)


if __name__ == "__main__":
    # Input parameters
    s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    k = 10
    # Instantiating object
    a = Solution().findRepeatedDnaSequences(s, k)
    # Printing out solution
    logger.info(f"Output: {a}")
