def depthFirstSearch(V, E):
    def dfs(node, temp):
        visited[node] = True
        temp.append(node)
        for ch in adjlist[node]:
            if not visited[ch]: dfs(ch, temp)

    adjlist = dict()
    for i in range(V): adjlist[i] = []
    for _ in range(E):
        node, edge = map(int, input().split(' '))
        adjlist[node].append(edge)
        adjlist[edge].append(node)

    ans = []
    visited = [False for _ in range(V)]
    for i in range(len(visited)):
        if not visited[i]:
            temp = []
            dfs(i, temp)
            ans.append(temp.copy())

    return ans


V, E = map(int, input().split(' '))
ans = depthFirstSearch(V, E)
print()
print(len(ans))
for ch in ans: print(*sorted(ch))
'''    
10 9
1 0
2 0
3 0
4 0
5 0
6 0
7 0
8 0
9 0

1
0 1 2 3 4 5 6 7 8 9
'''

'''
5 6
0 4
2 0
2 4
3 0
3 2
4 3

2
0 2 3 4 
1 
'''

'''
9 9
0 8
1 6
1 7
1 8
6 0
7 3
7 4
8 7
2 5

2
0 1 3 4 6 7 8 
2 5 
'''

'''
10 5
9 0
8 1
7 2
6 3
5 4

5
0 9 
1 8 
2 7 
3 6 
4 5 
'''
