
def solution(n, lost, reserve):
    _reserve = set([r for r in reserve if r not in lost])
    _lost = set([l for l in lost if l not in reserve])
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)

from collections import deque
a = deque()
a.append("C")
a.rotate()
from itertools import product
#for rs in product((-1,1), repeat=len(name)-1):
#    print(rs)

def solution(name):
    def alpha(ap):
        if ord(ap) > 78:
            return 90 - ord(ap) + 1
        else:
            return ord(ap) - 65
    alpha_c = list(map(alpha, name))
    len_a = sum(map(lambda x: x!=0,alpha_c))
    comp = 0
    alpha_d = sum(alpha_c)
    move_d = 0
    while comp != len_a-1:
        for n,i in enumerate(name):
            if n ==0:
                continue
            if i !='A':
                break
        for n2,i2 in enumerate(reversed(name),1):
            if i2 !='A':
                break
        if n > n2:
            move_d += n2
            print(f"n2 {n2}")
            name = name[-n2:] + name[:-n2]
        else:
            move_d += n
            print(f"n {n}")
            name = name[n:] + name[:n]
        comp +=1
    return move_d + alpha_d

def solution(name):
    if set(name) == {'A'}:
        return 0

    answer = float('inf')
    for i in range(len(name) // 2): # 반 이상 움직일 필요 없음
        left_moved = name[-i:]+name[:-i]
        right_moved = name[i:]+name[:i]
        for n in [left_moved, right_moved[0]+right_moved[:0:-1]]:
            while n and n[-1] == 'A':
                n = n[:-1]

            row_move = i + len(n)-1
            col_move = 0
            for c in map(ord, n):
                col_move += min(c - 65, 91 - c)

            answer = min(answer, row_move + col_move)

    return answer


def solution(number, k):
    stack = [number[0]]
    for num in number[1:]:
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)


from collections import deque
def solution(people, limit):
    answer = 0
    deq = deque(sorted(people))
    while deq:
        if len(deq) == 1:
            answer += 1
            break
        if deq[0] + deq[-1] <= limit:
            deq.pop()
            deq.popleft()
        else:
            deq.pop()
        answer += 1
    return answer

people, limit = [70, 50, 80, 50],100


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

def solution(n, costs):
    parent = [i for i in range(n)]
    cnt = 0
    cost = 0
    costs = sorted(costs,key=lambda x: x[2])
    for x in costs:
        a = x[0]
        b = x[1]
        print(parent)
        if not linked(parent, a, b):
            cnt += 1
            cost += x[2]
            print(a, b, x[2])

        if cnt == n-1:
            break
    return cost
n,costs = 4,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
