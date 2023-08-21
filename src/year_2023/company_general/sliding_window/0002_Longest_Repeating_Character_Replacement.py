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
from collections import defaultdict

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s]: %(message)s",
)
logger.setLevel(logging.INFO)


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        You are given a string s and an integer k. You can choose any
        character of the string and change it to any other uppercase
        English character. You can perform this operation at most k times.

        Return the length of the longest substring containing the same
        letter you can get after performing the above operations.

        Parameters
        --------------

        Returns
        --------------

        Notes / Steps
        --------------
        1.  Initialize variables to keep track of the frequency of each
            character, plus initialize the 'left' and 'right' pointers. These
            will be used to determine how many characters we can swap
            in a given window of certain length.
        2.  Start iterating at the first index.
        3.  Update the frequency of the character in the specified hashmap.
        4.  Perform a while loop that calculates the length of the longest
            substring while keeping track of the number of available
            instances per character in the window.


        Links
        --------------
        https://leetcode.com/problems/longest-repeating-character-replacement/description/


        Raises
        --------------
        """
        # --- Initialize the counter
        # Two pointers
        left = right = 0
        # Set for keeping track of the available characters to swap
        character_set = defaultdict(int)
        # Variable to keep track of the maximum frequency
        max_frequency = 0
        # Variable to keep track of the length of the longest substring
        max_count = 0

        # --- Iterating over each character
        for right in range(len(s)):
            # Determining the character
            character = s[right]
            # Updating the number of available instances for given letter
            character_set[character] += 1
            # Determine the maximum frequency
            max_frequency = max(max_frequency, character_set[character])

            # Determining the number of 'available' letters to swap.
            while (right - left + 1) - max_frequency > k:
                # Updating the number of available letters to swap
                character_set[character] -= 1
                # Moving to the left of the window
                left += 1

            # Updating the length of the longest substring
            max_count = max(max_count, right - left + 1)

        return max_count


if __name__ == "__main__":
    # Input parameters
    s = "ABAB"
    k = 2
    # Instantiating object
    a = Solution().characterReplacement(s=s, k=k)
    # Printing out solution
    logger.info(f"a: {a}")
