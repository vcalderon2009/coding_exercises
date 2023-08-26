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
from typing import Optional, Tuple

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
    def reverseKGroup(
        self,
        head: Optional[ListNode],
        k: int,
    ) -> Optional[ListNode]:
        """
        Given the head of a linked list, reverse the nodes of the list ``k``
        at a time, and return the modified list.

        ``k`` is a positive integer and is less than or equal to the length
        of the linked list. If the number of nodes is not a multiple of ``kk``
        then left-out nodes, in the end, should remain as it is.

        You may not alter the values in the list's nodes, only nodes
        themselves may be changed.

        Parameters
        --------------

        Returns
        --------------


        Links
        --------------
        https://leetcode.com/problems/reverse-nodes-in-k-group/

        Educative:
            https://www.educative.io/courses/grokking-coding-interview-patterns-python/solution-reverse-nodes-in-k-group#Just-the-code


        Raises
        --------------

        NOTES
        ----------
        This answer still needs some work.
        """

        def reverse_linked_list_k_nodes(
            origin: ListNode,
            k: int,
        ) -> Tuple[ListNode, ListNode]:
            """

            Returns
            ---------
            curr : ListNode
                Current Node

            prev : ListNode
                Previous node.
            """
            prev = None
            curr = origin

            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            return prev, curr

        # Initilize dummy Node
        dummy = ListNode(next=head)
        # --- Initializing the pointer and tracker nodes.
        # NOTE: The 'tracker' is the one that will count the number of
        # nodes traversed.
        ptr = dummy

        while ptr:
            # Initializing tracker node
            tracker = ptr
            # Traversing 'k' elements
            for _ in range(k):
                # Breaking out of the loop if there aren't enough nodes
                if not tracker:
                    break
                # Updating the 'tracker' object
                tracker = tracker.next

            # Break out of the while look if the 'tracker' element is not valid
            if not tracker:
                break

            # --- Reversing the linked list for 'k' nodes
            previous, current = reverse_linked_list_k_nodes(
                origin=ptr.next,
                k=k,
            )

            # Rearranging variables
            last_node_of_reversed_group = ptr.next
            last_node_of_reversed_group.next = current
            ptr.next = previous
            ptr = last_node_of_reversed_group

        return dummy.next


if __name__ == "__main__":
    # Input parameters
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
    a = Solution().reverseKGroup(head=head, k=k)
    # Printing out solution
    logger.info(f"Solution: {a}")
