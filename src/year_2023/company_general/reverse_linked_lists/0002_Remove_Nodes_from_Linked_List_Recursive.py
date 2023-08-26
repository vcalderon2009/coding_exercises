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
    def __init__(self) -> None:
        self.n = 0

    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        You are given the head of a linked list.

        Remove every node which has a node with a strictly greater
        value anywhere to the right side of it.

        Return the head of the modified linked list.

        Parameters
        --------------

        Returns
        --------------


        Links
        --------------
        https://leetcode.com/problems/remove-nodes-from-linked-list/description/

        Raises
        --------------
        """
        # Checking if node is empty
        if not head:
            logger.info(f">>> {self.n} - Returning NONE\n")
            return None

        # Recursively iterating over each node
        logger.info(
            f">>> {self.n} - BEFORE     : head: {head.val} | Next: {head.next.val if head.next else ''}"  # noqa: E501
        )
        head.next = self.removeNodes(head.next)
        logger.info(
            f">>> {self.n} - AFTER       : head: {head.val} | Next: {head.next.val if head.next else ''}"  # noqa: E501
        )

        if head.next and head.next.val > head.val:
            logger.info(
                f">>> {self.n} - CONDITIONAL : head: {head.val} | Next: {head.next.val if head.next else ''}"  # noqa: E501
            )
            return head.next

        logger.info(
            f">>> {self.n} - FINAL       : head: {head.val} | Next: {head.next.val if head.next else ''}"  # noqa: E501
        )
        self.n += 1
        return head


class SolutionTwo:
    def __init__(self) -> None:
        self.n = 0

    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        # Iterating over each node recursively
        head.next = self.removeNodes(head.next)

        # NOTE: After this, the node is valid and we must compare the value
        # of the node to it's next value. If the next value is larger than
        # the current node's value, then that would violate the criteria
        # for keeping the node, and we must remove it and make the
        # node's next value the one before.

        return head.next if head.next and head.val < head.next.val else head


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
    # a = Solution().removeNodes(head=head)
    a = SolutionTwo().removeNodes(head=head)
    # Printing out solution
    logger.info(f"Solution: {a}")
