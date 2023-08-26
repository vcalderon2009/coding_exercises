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
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        You are given the head of a linked list.

        Remove every node which has a node with a strictly greater value
        anywhere to the right side of it.

        Return the head of the modified linked list.

        Parameters
        --------------


        Returns
        --------------


        Links
        --------------
        https://leetcode.com/problems/remove-nodes-from-linked-list/


        Raises
        --------------

        Examples
        --------------
            Input: head = [5,2,13,3,8]
            Output: [13,8]

            Input: head = [1,1,1,1]
            Output: [1,1,1,1]

        Steps
        ---------------
        1.  Define the stac.
        2.  Define a `curr` variable that equals the `head` node.
        3.  We'll check the stack's last element and compare it to the
            current value. We'll continue until the current node's value
            is larger than the last element in the stack, and we'll keep
            removing the elements from right of the stack until then.
        4.  Once we've found new value, we'll add it to the stack.
        5.  Update our pointer to the current number
        6.  Create a new node ``dummy``.
        7.  Return the dummy's next node.
        """
        # Define variables
        stack = []
        curr = head

        # Iterating over current value
        while curr:
            # Check if the last element of the stack (if any) is smaller
            while stack and stack[-1].val < curr.val:
                stack.pop()

            # Add element to the stack
            stack.append(curr)

            # Update pointer
            curr = curr.next

        # Defining dummy node
        dummy = ListNode()
        curr = dummy

        for node in stack:
            # Removing node from stack
            curr.next = node
            curr = curr.next

        return dummy.next


if __name__ == "__main__":
    # Input parameters
    head_values = [5, 2, 13, 3, 8]
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
    a = Solution().removeNodes(head=head)
    # Printing out solution
    logger.info(f"Solution: {a}")
