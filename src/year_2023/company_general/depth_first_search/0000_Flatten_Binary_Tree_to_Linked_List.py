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
from typing import Optional

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s]: %(message)s",
)
logger.setLevel(logging.INFO)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Given the root of a binary tree, flatten the tree into a "linked list":

            -   The "linked list" should use the same TreeNode class where
                the right child pointer points to the next node in the list
                and the left child pointer is always null.
            -   The "linked list" should be in the same order as a pre-order
                traversal of the binary tree.

        Parameters
        --------------

        Returns
        --------------


        Links
        --------------
        https://leetcode.com/problems/flatten-binary-tree-to-linked-list/


        Raises
        --------------
        """
        if not root:
            return None

        # Defining the current node
        curr = root

        while curr:
            # Check if there is a left-side tree
            if curr.left:
                # Saving the current left tree
                last = curr.left

                # Iterating until we find the right-most tree
                while last.right:
                    last = last.right

                # Reorganizing pointers
                last.right = curr.right
                curr.right = curr.left
                curr.left = None

            # Update pointer
            curr = curr.right

        return root


if __name__ == "__main__":
    # Input parameters
    root = [1, 2, 5, 3, 4, None, 6]
    # Instantiating object
    a = Solution().test_function()
    # Printing out solution
    logger.info(f"Solution: {a}")
