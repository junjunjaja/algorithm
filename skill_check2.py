"""
땅따먹기 게임을 하려고 합니다. 땅따먹기 게임의 땅(land)은 총 N행 4열로 이루어져 있고, 모든 칸에는 점수가 쓰여 있습니다. 1행부터 땅을 밟으며 한 행씩 내려올 때, 각 행의 4칸 중 한 칸만 밟으면서 내려와야 합니다. 단, 땅따먹기 게임에는 한 행씩 내려올 때, 같은 열을 연속해서 밟을 수 없는 특수 규칙이 있습니다.

예를 들면,

| 1 | 2 | 3 | 5 |

| 5 | 6 | 7 | 8 |

| 4 | 3 | 2 | 1 |

로 땅이 주어졌다면, 1행에서 네번째 칸 (5)를 밟았으면, 2행의 네번째 칸 (8)은 밟을 수 없습니다.

마지막 행까지 모두 내려왔을 때, 얻을 수 있는 점수의 최대값을 return하는 solution 함수를 완성해 주세요. 위 예의 경우, 1행의 네번째 칸 (5), 2행의 세번째 칸 (7), 3행의 첫번째 칸 (4) 땅을 밟아 16점이 최고점이 되므로 16을 return 하면 됩니다.

제한사항
행의 개수 N : 100,000 이하의 자연수
열의 개수는 4개이고, 땅(land)은 2차원 배열로 주어집니다.
점수 : 100 이하의 자연수
입출력 예
land	answer
[[1,2,3,5],[5,6,7,8],[4,3,2,1]]	16
입출력 예 설명
입출력 예 #1
문제의 예시와 같습니다.

"""
from collections import deque
from copy import deepcopy
import random
land = deque([[1,2,3,5],[5,6,7,8],[4,3,2,1]])
land = deque([[1,2,3,5],[5,6,7,8],[4,3,2,1],[8,7,6,5]])
class Land(object):
    def __init__(self,land):
        self.land = land
        self.n_row = len(self.land)
        self.n_col = 4
    def one_search(self,point):
        assert len(point) == self.n_row,(len(point),self.n_row)
        return sum([self.land[n][i] for n,i in enumerate(point)])
    def greed(self):
        if len(self.queue) ==0:
            self.queue.append(random.randint(0,3))
        else:
            n = self.queue[-1]
            while True:
                n_1 =random.randint(0, 3)
                if n !=n_1:
                    self.queue.append(n_1)
                    break
    def greed_search(self):
        self.queue = []
        for i in range(self.n_row):
            self.greed()
        return tuple(self.queue)

    def run(self):
        self.queues = set()
        while len(self.queues) != ((4)**(self.n_row) - (4 + (self.n_row-1)*4 + (self.n_row-2)*4)):
            queue = self.greed_search()
            self.queues.add(queue)
        max_ = 0
        max_q = None
        for i in self.queues:
            n = self.one_search(i)
            if max_ < n:
                max_q = i
                max_ = n
        return max_,max_q



self = Land(land)
self.land
self.run()

self.queues
self.next_check(1)
self.queue
self.run()
self.result



self.one_search([1,1,1])

def solution(land):
    answer = 0

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return answer