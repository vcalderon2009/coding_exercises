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


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        """
        Given a reference of a node in a connected undirected graph.

        Return a deep copy (clone) of the graph.

        Each node in the graph contains a value (int) and a list (List[Node])
        of its neighbors.

        class Node {
            public int val;
            public List<Node> neighbors;
        }

        Parameters
        --------------

        Returns
        --------------


        Links
        --------------
        https://leetcode.com/problems/clone-graph/


        Raises
        --------------
        """
        visited = {}

        def dfs(node):
            # Check if the node is valid
            if not node:
                return node

            # Check if the value has already been observed
            if node in visited:
                return visited[node]

            # Adding node to the visited dictionary
            visited[node] = Node(val=node.val, neighbors=[])

            # Looping over each neighbor, if they exist
            for neighbor in node.neighbors:
                visited[node].neighbors.append(dfs(neighbor))

            return visited[node]

        return dfs(node)


if __name__ == "__main__":
    # Input parameters
    adjList = [[2, 4], [1, 3], [2, 4], [1, 3]]
    # Instantiating object
    a = Solution().test_function()
    # Printing out solution
    logger.info(f"Solution: {a}")
