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

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s]: %(message)s",
)
logger.setLevel(logging.INFO)


class Solution:
    def isHappy(self, n: int) -> bool:
        """
        Write an algorithm to determine if a number n is happy.

        A happy number is a number defined by the following process:

        -   Starting with any positive integer, replace the number by the
            sum of the squares of its digits.
        -   Repeat the process until the number equals 1 (where it will stay),
            or it loops endlessly in a cycle which does not include 1.
        -   Those numbers for which this process ends in 1 are happy.

        Return ``true`` if n is a happy number, and ``false`` if not.

        Notes
        --------------
        Values of ``n`` must be [1, 2^31 - 1] --> All positive values.

        Parameters
        --------------

        Returns
        --------------
        is_happy : bool
            If ``True``, the input number ``n`` is a happy number. Otherwise,
            it's not a `happy` number.

        Links
        --------------
        https://leetcode.com/problems/happy-number/description/


        Raises
        --------------
        """

        def get_component_total_sum(number: int) -> int:
            """
            Function to calculate the total sum of the different components
            of ``number``.

            Parameters
            -------------
            number : int
                Number, for which to calculate the sum of the squares of its
                components / digits.

            Returns
            -----------
            total_sum : int
                Total sum of the squares of the components of ``number``.
            """
            # Initializing total sum
            total_sum = 0

            # --- Calculating the sum of the components until it converges
            while number > 0:
                # Splitting into components
                number, digit = divmod(number, 10)
                # Calculating total sum
                total_sum += digit * digit

            return total_sum

        # 1.    Define a set to keep track of the observed numbers
        observed_sums = set()

        # 2.    Start computing the sum of squares of the components of ``n``.
        while n > 1:
            # Compute the total sum of the squares
            n = get_component_total_sum(number=n)

            # Determine if ``n`` is a `happy` number or not.
            if n > 1 and n in observed_sums:
                return False

            # Add total sum to set if not observed yet.
            observed_sums.add(n)

        return True


if __name__ == "__main__":
    # Input parameters
    n = 19
    # Instantiating object
    result = Solution().isHappy(n=n)
    # Printing out solution
    logger.info(f"result: {result}")
