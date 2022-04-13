from collections import deque

def BFS_with_adj_list(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            queue += graph[n] - set(visited)
    return visited
graph_list = {1: set([3, 4]),
              2: set([3, 4, 5]),
              3: set([1, 5]),
              4: set([1]),
              5: set([2, 6]),
              6: set([3, 5])}
root_node = 1
print(BFS_with_adj_list(graph_list, root_node))


class Tree(object):
    def __init__(self, x, l=None, r=None): # 'None' means empty Node
        self.x = x	# value of Node
        self.l = l	# left child of Node
        self.r = r	# right child of Node

T = Tree(4, Tree(5, Tree(4, Tree(5, None, None), None), None), Tree(6, Tree(1, None, None), Tree(6, None, None)))
solution(T)
def solution(T):
    distinct = {1: set([])}
    stack = [(T, [T], set([T.x]))]
    #[방문하려는 노드, 지금까지의 경로, 경로 중 볼 수 있는 서로 다른 값]
    i = 1  # number of path
    while stack:  # DFS
        n, path, value = stack.pop()
        if n.l == None and n.r == None:  # leaf node
            distinct[i] = value
            i = i + 1
        else:
            if n.r != None:
                stack.append((n.r, path + [n.r], value | set([n.r.x])))
            if n.l != None:
                stack.append((n.l, path + [n.l], value | set([n.l.x])))

    answer = 1

    for key in distinct.keys():
        temp = len(distinct[key])
        if temp > answer:
            answer = temp
    print(distinct)
    return answer


def solution(numbers, target):
    answer = 0
    print("level 0 %s "% hex(id(answer)))
    def BFS(result,numbers,id_):
        nonlocal answer
        print("level %s %s " % (id_,hex(id(answer))))
        if len(numbers) <= id_:
            if result == target:
                #print(result,target)
                answer = answer + 1
        else:
            BFS(result+numbers[id_],numbers,id_+1)
            BFS(result-numbers[id_], numbers, id_+1)
    BFS(0, numbers, 0)
    return answer


numbers = [1, 1, 1, 1, 1]
target = 3

solution(numbers, target)

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


