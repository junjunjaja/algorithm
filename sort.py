
from collections import deque
import heapq
array, commands = [1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]
def solution(array, commands):
    answer = []
    commands = deque(commands)
    while len(commands):
        st,end,k = commands.popleft()
        answer.append(heapq.nsmallest(3,array[st-1:end])[-1])
    return answer

def solution(numbers):
    answer = ''
    sum_ = 0
    tmp = []
    for number in numbers:
        c = (str(number) * 4)[:4]
        length = len(str(number))
        tmp.append((c, length))
    tmp.sort(reverse=True)
    for (c, length) in tmp:
        sum_ += int(c)
        if sum_ == 0:
            return '0'
        answer += c[:length]
    return answer
numbers = [3, 30, 34, 5, 9]
solution(numbers)

citations= [3, 0, 6, 1, 5]
citations = [2]
citations = sorted(citations)
all_len = len(citations)
idx = all_len//2+1
h = citations[idx]
low_num = len(citations) - idx + 1
high_num = len(citations) - idx + 1
if (len(citations[h-1:]) == len(citations[:h]))

def solution(citations):
    #
    answer = 0
    return answer