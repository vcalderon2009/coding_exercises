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


class SolutionNew:
    def reverseBetween(
        self,
        head: Optional[ListNode],
        left: int,
        right: int,
    ) -> Optional[ListNode]:
        """
        Given the head of a singly linked list and two integers
        left and right where left <= right, reverse the nodes of the
        list from position left to position right, and return the
        reversed list.

        Parameters
        --------------

        Returns
        --------------


        Links
        --------------
        https://leetcode.com/problems/reverse-linked-list-ii/


        Steps
        --------------
        """
        if not head:
            return

        # Create pointers
        dummy = ListNode(0, head)

        # Creating a pointer to keep track of the nodes
        leftPrev, curr = dummy, head
        # Moving pointers to the 'left' position
        for _ in range(left - 1):
            leftPrev, curr = curr, curr.next

        # 2.    Now we need to reverse the list until we get to the 'right'
        #       position.
        prev = None
        for _ in range(right - left + 1):
            tmpNext = curr.next
            curr.next = prev
            prev = curr
            curr = tmpNext

        # 3.    Fix the connections of the reversed linked list
        leftPrev.next.next = curr
        leftPrev.next = prev

        return dummy.next


if __name__ == "__main__":
    # Input parameters
    left = 2
    right = 4
    head = [1, 2, 3, 4, 5]
    head_values = [1, 2, 3, 4, 5]
    k = 3

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
    a = SolutionNew().reverseBetween(head=head, left=left, right=right)
    # Printing out solution
    logger.info(f"Solution: {a}")
