"""
문제 설명
정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.

제한 사항
n은 0 이상 3000이하인 정수입니다.
입출력 예
n	return
12	28
5	6
입출력 예 설명
입출력 예 #1
12의 약수는 1, 2, 3, 4, 6, 12입니다. 이를 모두 더하면 28입니다.

입출력 예 #2
5의 약수는 1, 5입니다. 이를 모두 더하면 6입니다.
"""


def get_prime(n):
    cut_num = n // 2
    answer = set()
    if n >=4:
        for i in range(1,cut_num):
            n1 = n % i
            n2 = n // i
            if n1  == 0:
                answer |= set([i,n2])
        return sum(answer)
    elif n >1:
        return n+1
    else:
        return 1 if n else 0

n = 50
answer = n

from collections import deque
class Board(object):
    def __init__(self,board,moves):
        self.n = len(board)
        self.board_c = [deque([i[k] for i in board if i[k]]) for k in range(self.n)]
        self.moves = moves
        self.result_col  = deque()
        self.result = 0
    def moving(self):
        for mv in self.moves:
            try:
                doll = b.board_c[mv-1].popleft()
                if len(self.result_col):
                    pop = True if self.result_col[-1] == doll else False
                    if pop:
                        self.result_col.pop()
                        self.result +=2
                    else:
                        self.result_col.append(doll)
                else:
                    self.result_col.append(doll)
            except IndexError:
                pass


board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
b = Board(board,moves)
b.moving()


from collections import defaultdict
c = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
cloth = defaultdict(list)
answer = 1
for k, j in c:
    cloth[j].append(k)
for i in list(map(lambda x: len(x) + 1, cloth.values())):
    answer *= i


from copy import copy
from copy import deepcopy as copy
import ctypes


def get_object_by_id(object_id):
    obj = ctypes.cast(object_id, ctypes.py_object).value
    print(obj)
    return

class Node:
    def __init__(self,item,data,target,sum=0,parent=None):
        self.target = target
        self.parent = parent
        if self.parent is None:
            self.result = 0
        else:
            self.result = self.parent.result
        self.item = item
        sum += self.item
        print(data,sum)
        if len(data) >=2:
            item = data[0]
            self.left = Node(item,data[1:],target,sum,self)
            self.right = Node(-item,data[1:],target,sum,self)
        else:
            self.data = item
            if (sum+self.data == target):
                self.result += 1
                print([], sum + self.data)
            if (sum-self.data == target):
                self.result += 1
                print([], sum-self.data)
        if self.parent is not None:
            self.parent.result = self.result

    import numpy as np
    mat = [[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]
    class maxmat(object):
        def __init__(self,mat):
            self.mat = mat
            self.col = len(mat)
            self.row = len(mat[0])
            self.sum_ = sum([sum(i) for i in self.mat])
            if self.sum_ > 1:
                for k in range(1,self.sum_):
                    if k**2 >=self.sum_:
                        break
                k -= 1
            else:
                k = 1
            self.result = self.kernel(k)

        def kernel(self,num):
            for y in range(self.col - num+1):
                for x in range(self.row - num+1):
                    ret = 1
                    num_y = y + num
                    num_x = x + num
                    for yy in range(y, num_y):
                        ret *= all(self.mat[yy][x:num_x])

                    if ret:
                        return num **2
            else:
                return self.kernel(num-1)

    self = maxmat(mat)
    self.kernel(5)
