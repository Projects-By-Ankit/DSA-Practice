# from typing import List
#
#
# def bfsTraversal(n: int, adj: List[List[int]]) -> List[int]:
#     # write your code here
#     print(adj)
#     ans = []
#     queue = []
#     adjlist = dict()
#
#     for i in range(n):
#         adjlist[i] = []
#     for i in range(len(adj)):
#         adjlist[i].extend(adj[i])
#
#     def helper(node):
#         visited[node] = True
#         queue.append(node)
#         while queue:
#             print(queue)
#             nd = queue.pop(0)
#             ans.append(nd)
#             for ch in adjlist[nd]:
#                 if not visited[ch]:
#                     queue.append(ch)
#                     visited[ch] = True
#
#     visited = [False for _ in range(n)]
#     for node in range(len(visited)):
#         if not visited[node]:
#             print(node, end=' ')
#             helper(node)
#     return ans
#
#
# # print(bfsTraversal(8, [[1, 2, 3], [4, 7], [5], [6], [], [], [], []]))
#
# print(bfsTraversal(4, [[1, 2, 3], [2], [], []]))

from typing import List


def bfs_traversal(n: int, adj: List[List[int]]) -> List[int]:
    # write your code here
    ans = []
    queue = []

    def helper(node):
        visited[node] = True
        queue.append(node)
        while queue:
            nd = queue.pop(0)
            ans.append(nd)
            for ch in adj[nd]:
                if not visited[ch]:
                    queue.append(ch)
                    visited[ch] = True

    visited = [False for _ in range(n)]
    helper(0)
    return ans
