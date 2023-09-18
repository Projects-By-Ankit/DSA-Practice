def cycleDetection(edges, n, m):
    def CycleDFS(node, pr):
        visited[node - 1] = True
        for ch in adjlist[node]:
            if not visited[ch - 1]:
                ans = CycleDFS(ch, node)
                if ans: return True
            elif ch != pr:
                return True
        return False

    adjlist = dict()
    for vertices in range(1, n + 1): adjlist[vertices] = []
    for edge in edges:
        u, a = edge[0], edge[1]
        adjlist[u].append(a)
        adjlist[a].append(u)
    visited = [False] * n
    parent = dict()

    for node in range(len(visited)):
        if not visited[node]:
            ans = CycleDFS(node + 1, -1)
            if ans: return 'Yes'
    return 'No'


'''
3
3 2
1 2
2 3
4 0 
4 3
1 4
4 3
3 1

No
No
Yes

3
6 4
1 6
2 3
3 4
2 4
3 2
2 1
3 1
4 4
1 3
1 2
2 4
3 4

Yes
No
Yes

3
2 0
7 4
1 2
5 6
6 7
5 7
5 7
1 2
2 3
3 4
4 5
5 1
2 4
3 5

No
Yes
Yes

3
5 4
1 4
3 1
5 4
5 1
6 5
1 2
2 3
4 3
5 4
6 5
1 0


Yes
No
No
'''
