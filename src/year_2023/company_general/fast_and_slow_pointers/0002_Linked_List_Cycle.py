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
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Given head, the head of a linked list, determine if the linked list
        has a cycle in it.

        There is a cycle in a linked list if there is some node in the list
        that can be reached again by continuously following the next pointer.
        Internally, pos is used to denote the index of the node that tail's
        next pointer is connected to. Note that pos is not passed as a
        parameter.

        Return ``true`` if there is a cycle in the linked list.
        Otherwise, return ``false``.

        Parameters
        --------------
        head : ListNode
            Head of the linked list.

        Returns
        --------------
        is_cycle : bool
            If ``True``, there is a cycle in the linked list.
            Otherwise, there is no cycle present.

        Links
        --------------
        https://leetcode.com/problems/linked-list-cycle/


        Raises
        --------------
        """
        # --- Edge cases
        if head is None:
            return False

        # --- Defining slow and fast pointers
        slow = head
        fast = head.next

        # Loop through the nodes
        while slow != fast:
            # Check that the current values are valud
            if fast is None or fast.next is None:
                return False

            # Increasing pointers
            slow = slow.next
            fast = fast.next.next

        return True


if __name__ == "__main__":
    # Input parameters
    head_values = [1, 2]
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
    a = Solution().hasCycle(head=head)
    # Printing out solution
    logger.info(f"\n\n>>> OUTPUT: {a}\n\n")
