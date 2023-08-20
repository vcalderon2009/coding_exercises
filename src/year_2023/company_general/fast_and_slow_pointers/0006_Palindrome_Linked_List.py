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


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        Given the head of a singly linked list, return true if it is a
        palindrome or false otherwise.

        Parameters
        --------------
        head : ListNode
            Head node from the linked list.

        Returns
        --------------
        is_palindrome : bool
            If ``True``, the linked list is a valid palindrome. Otherwise,
            it is not.

        Links
        --------------
        https://leetcode.com/problems/palindrome-linked-list/


        Raises
        --------------
        """

        # Initializing pointers
        slow = head
        fast = head

        # Finding the middle of the linked list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # --- We now have to reverse the linked list
        prev = None
        curr = slow

        while curr:
            # Temporarily saving the next node
            nxt = curr.next
            # Updating nodes
            curr.next = prev
            prev = curr
            curr = nxt

        # Now we compare the first half of the linked list to the
        # reversed second half
        first_half, reversed_second_half = head, prev
        while first_half and reversed_second_half:
            if first_half.val != reversed_second_half.val:
                return False
            # Updating pointers
            first_half = first_half.next
            reversed_second_half = reversed_second_half.next

        return True


if __name__ == "__main__":
    # Input parameters
    head_values = [1, 2, 2, 3, 4, 5, 1]
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
    a = Solution().isPalindrome(head=head)
    # Printing out solution
    logger.info(f"Result: {a}")
