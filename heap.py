# 힙
# 최솟값이나 최댓값을 빠르게 찾아내기 위해 완전 이진 트리를 기반으로 하는 트리

"""
최대 힙
부모 노드가 자식 노드 보다 큰 힙

Heapify Algorithm
특정 하나의 노드에 대해서 수행
while 자식노드 존재
    자식 노드 중 더 큰 자식과 자신의 위치 변경

하나의 노드를 제외하고는 최대 힙이 구성되어 있는 상태'라고 가정
"""
#heap 정렬구현
def heap(s):
    stack = s[:]
    # 최대 heap 구성
    for i in range(1,len(stack)):
        c = i
        while c !=0:
            root = int((c-1)/2)
            if stack[root] < stack[c]:
                temp = stack[root]
                stack[root] = stack[c]
                stack[c] = temp
            c = root
    print(f"최대 heap {stack}")
    for i in range(len(stack)-1,0,-1):
        # i에 대해 정렬하고 i를 제외 한 채로 heapify 알고리즘 수행
        temp = stack[0]
        stack[0] = stack[i]
        stack[i] = temp
        root = 0
        c = 1
        print(f"정렬 {(0,i)}, {stack}")
        while c < i:
            c = 2*root + 1
            if (c < i-1 & stack[root] <stack[c]):
                temp = stack[root]
                stack[root] = stack[c]
                stack[c] = temp
            root = c
        print(f"heapify {stack}")
    return stack

#heap module
from collections import deque
stack = list(map(int,"7 6 5 8 3 5 9 1 6".split(" ")))
import heapq
heap = []
heapq.heapify(stack)
heapq.heappush(heap,1)
for i in stack:
    heapq.heappush(heap,i)
#최대 힙 tuple 이용해서 -값 이용
import heapq
nums = [4, 1, 7, 3, 8, 5]
heap = []
for num in nums:
  heapq.heappush(heap, (-num, num))  # (우선 순위, 값)

while heap:
  print(heapq.heappop(heap)[1])  # index 1

import heapq
#매운맛 문제
def solution(scoville, K):
    heapq.heapify(scoville)
    result = 0
    while True:
        if not len(scoville):
            return result
        elif scoville[0] >=K:
            return result
        elif len(scoville)==1:
            return -1
        else:
            ingred = [heapq.heappop(scoville) for _ in range(2)]
            s = ingred[0]+ingred[1]*2
            result +=1
            heapq.heappush(scoville,s)
    return result
scoville, K = [1, 2, 3, 9, 10, 12],7
solution(scoville, K)

import heapq
#디스크 문제
def solution(jobs_):
    jobs = jobs_[:]
    answer = 0
    time = 0
    ready_heap = []
    heapq.heapify(jobs)
    while len(jobs) or len(ready_heap):
        while len(jobs):
            if jobs[0][0] <= time:
                get_time,job_taken = heapq.heappop(jobs)
                heapq.heappush(ready_heap,(job_taken,get_time))
            else:
                break
        if len(ready_heap):
            heapq.heapify(ready_heap)
            running,taken = heapq.heappop(ready_heap)
            time += running
            answer += time - taken
            print(f"{answer},{time},{jobs}")
        else:
            time += 1
    return int(answer/len(jobs_))
jobs = [[0, 3], [1, 9], [2, 6]]
solution(jobs)

import heapq

def solution(operations):
    answer = []
    max_heap = []
    for i in operations:
        if 'I' in i:
            dat = int(i.replace("I ", ""))
            heapq.heappush(answer,dat)
            heapq.heappush(max_heap, (-dat,dat))
        else:
            if len(answer):
                if "D -" in i:
                    heapq.heappop(answer)
                    del answer[-1]
                else:
                    heapq.heappop(max_heap)
    if len(answer):
        return [max_heap[0][1],answer[0]]
    else:
        return [0,0]
operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
solution(operations)
operations = ["I 16", "D 1"]




