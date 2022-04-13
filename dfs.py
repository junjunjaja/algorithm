def find_path(parent, n):
    if parent[n] == n: #자기 자신이 현재 Tree의 parent
        return n
    parent[n] = find_path(parent, parent[n]) #가장 최고 node 찾기 위해 recur
    return parent[n]

def linked(parent, a, b):
    a = find_path(parent, a)
    b = find_path(parent, b)
    if a == b:  #두 node 가 같다면 이미 연결 -> True
        return True
    if a < b:   #두 노드 중
        parent[a] = b
    else:
        parent[a] = b
    return False
from itertools import combinations
def solution(n, computers):
    parent = [i for i in range(n)]
    all_nodes = [(x,y,l) for x,dat in enumerate(computers) for y,l in enumerate(dat) if l  and y >x]
    for x in all_nodes:
        a = find_path(parent, x[0])
        b = find_path(parent, x[1])
        parent[b] = a
    for x in all_nodes:
        a = find_path(parent, x[0])
        b = find_path(parent, x[1])
        parent[b] = a
    return len(set(parent))

n, computers = 3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
solution(n, computers)

def solution(n, computers):
    answer = 0
    visited = [0 for i in range(n)]
    def dfs(computers, visited, start):
        stack = [start]
        while stack:
            print(visited)
            j = stack.pop()
            if visited[j] == 0:
                visited[j] = 1
            # for i in range(len(computers)-1, -1, -1):
            for i in range(0, len(computers)):
                if computers[j][i] ==1 and visited[i] == 0:
                    stack.append(i)
    i=0
    while 0 in visited:
        if visited[i] ==0:
            dfs(computers, visited, i)
            answer +=1
        i+=1
    return answer
n, computers = 3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
solution(n,computers)

def link_check(x,y):
    k = len(set(x) - set(y))
    if k ==1:
        return sum(x[i] == y[i] for i in range(len(x)))+1 == len(x)
    elif k ==0:
        k = len(set(y) - set(x))
        return True
    return False

from collections import deque
def solution(begin, target, words):
    if target not in set(words):
        return 0
    words_new = [begin] + words
    link_stack = [0]
    possible = []

    def DFS(start,target,level,link_stack):
        nonlocal possible
        if start == target:
            possible.append(level)
        else:
            should_visit = deque(sorted(set(range(len(words_new))) - set(link_stack)))
            while len(should_visit):
                t = should_visit.popleft()
                print(link_stack,should_visit,level)
                if link_check(words_new[t],start):
                    link_stack.append(t)
                    DFS(words_new[link_stack[-1]], target, level+1, link_stack)

    DFS(begin, target, 0, link_stack)
    if len(possible):
        return min(possible)
    else:
        return 0

begin, target, words = "hit",	"cog",	["hot", "dot", "dog", "lot", "log", "cog"]
words = words[::-1]
solution(begin, target, words)

def solution(tickets):
    tickets.sort(key=lambda x: (x[0], x[1]))
    def Node_down(ticket_,result):
        i = 0
        print(ticket_,result)
        if not len(ticket_):
            return result
        while (i < len(ticket_)) and (ticket_[i][0] != result[-1]):
            i +=1
        if i == len(ticket_):
            return []
        while ticket_[i][0] == result[-1]:
            results = Node_down(ticket_=ticket_[:i]+ticket_[i+1:], result=result+[ticket_[i][-1]])
            if results != []:
                return results
            i += 1
        return results
    return Node_down(ticket_=tickets,result=['ICN'])


tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
solution(tickets)

