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


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Given the head of a singly linked list, reverse the list, and
        return the reversed list.

        Parameters
        --------------

        Returns
        --------------


        Links
        --------------
        https://leetcode.com/problems/reverse-linked-list/


        Raises
        --------------

        Steps
        --------------
        1.  Define the current (`curr`), previous (`prev`), and next (`nxt`)
            nodes.
        2.  Define the `nxt` node to be curr's next node.
        3.  Define `prev` to be `curr`.
        4.  Define `curr` to `prev`

        Notes
        -----------
        Time complexity :   O(n)
        Space Complexity:   O(1)
        """
        # Defining pointers
        prev = None
        curr = head

        while curr:
            # Defining the `next`` node
            nxt = curr.next
            # Updating node's definitions
            curr.next = prev
            prev = curr
            curr = nxt

        return prev


if __name__ == "__main__":
    # Input parameters
    head_values = [1, 2, 3, 4, 5]
    nodes_arr = [[]]
    # Looping over values
    for idx, val in enumerate(head_values[::-1]):
        if idx == 0:
            nodes_arr[0] = ListNode(val)
        else:
            node = ListNode(val)
            node.next = nodes_arr[idx - 1]
            nodes_arr.append(node)
    # Specifying the head
    head = nodes_arr[-1]
    # Instantiating object
    a = Solution().reverseList(head=head)
    # Printing out solution
    logger.info(f"Solution: {a}")
