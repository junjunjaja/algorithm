from collections import deque
import heapq
def solution(answers):
    one = [1,2,3,4,5]*8
    two = [2,1,2,3,2,4,2,5]*5
    three = [3,3,1,1,2,2,4,4,5,5]*4
    kk = deque(zip(one,two,three))
    point = [0,0,0]
    answers = deque(answers)
    while len(answers):
        sol = answers.popleft()
        ans = kk.popleft()
        for n,a in enumerate(ans):
            if a == sol:
                point[n] +=1
        kk.append(ans)
    return [n+1 for n,i in enumerate(point) if i ==max(point)]

from itertools import permutations
def solution(numbers):
    def get_prime(num):
        denum = num // 2
        if denum ==1:
            return True
        for i in range(2,denum+1):
            if num%i ==0:
                return False
        return True
    int_num = list(numbers)
    all_pos = set()
    for i in range(1,len(numbers)+1):
        all_pos |= set(map(lambda x: int("".join(x)),permutations(int_num, i)))
    all_pos -= {0,1}
    return sum(map(get_prime,all_pos))

def solution(brown, yellow):
    x = yellow
    for y in range(1, yellow+1):
        if x*2 + y*2 + 4 == brown:
            return [x+2, y+2]
        x = yellow / (y+1)

def solution(brown, yellow):
    answer = []
    def y_to_b(yellow):
        yd = yellow//2
        if yd < 2:
            #yellow 3,2,1
            brown_need = yellow * 2 + 1 * 2 + 4
            if brown_need==brown:
                return (yellow+2,1+2)
        else:
            for yh in range(1,yd):
                if yellow %yh ==0:
                    yw = yellow//yh
                    brown_need = (yw+yh)*2+4
                    if brown_need == brown:
                        return [yw+2,yh+2]
    return y_to_b(yellow)