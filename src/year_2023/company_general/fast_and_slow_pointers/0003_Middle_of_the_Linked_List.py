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
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Given the head of a singly linked list, return the middle node of the
        linked list.

        If there are two middle nodes, return the second middle node.

        Parameters
        --------------
        head : ListNode
            Head of the LinkedList

        Returns
        --------------
        middle_node : ListNode
            Middle Node of the Linked list.

        Links
        --------------
        https://leetcode.com/problems/middle-of-the-linked-list/

        Raises
        --------------

        Notes
        ------------
        - The number of nodes in the list is in the range [1, 100].
        - 1 <= Node.val <= 100
        """
        # Returning head if head if the Linked list only has one Node
        if head.next is None:
            return head

        # Initializing fast and slow pointer
        fast_pointer = head
        slow_pointer = head

        # Traversing the linked list until we hit the end of it
        while True:
            if fast_pointer is None or fast_pointer.next is None:
                return slow_pointer

            # Increasing pointers
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next


if __name__ == "__main__":
    # Input parameters
    head_values = [1, 2, 3, 4, 5, 6, 7, 10]
    # head_values = [3, 2, 0, -4]
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
    a = Solution().middleNode(head=head)
    # Printing out solution
    logger.info(f"output: {a.val}")
