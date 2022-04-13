from collections import deque
def solution(progresses, speeds):
    all_queue = deque(maxlen=len(speeds))
    for p,s in zip(progresses,speeds):
        days = (100-p)//s
        real = (100-p)/s
        if real > days:
            days += 1
        all_queue.append(days)
    before_num = all_queue.popleft()
    answer = [1]
    while len(all_queue):
        s = all_queue.popleft()
        if before_num >=s:
            answer[-1] +=1
        else:
            answer.append(1)
            before_num = s
    return answer
progresses, speeds = [95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]


from collections import deque
def solution(priorities, location):
    answer = 0
    priorities = deque(priorities)
    while len(priorities):
        s = priorities.popleft()
        if not len(priorities) or (s >= max(set(priorities))):
            answer += 1
            if location ==0:
                return answer
            else:
                location -= 1
        else:
            priorities.append(s)
            if location == 0:
                location += len(priorities)-1
            else:
                location -= 1
    return answer
priorities, location = [1, 1, 9, 1, 1, 1],	0
solution(priorities, location)

from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0]*bridge_length,maxlen=bridge_length)
    truck_weights = deque(truck_weights)
    on_the_bridge =0
    bridge_weight = 0
    while len(truck_weights) or bridge_weight:
        pop_t = bridge.popleft()
        if pop_t:
            on_the_bridge -= 1
            bridge_weight -= pop_t
        if len(truck_weights):
            if (bridge_weight+truck_weights[0] <= weight) and on_the_bridge+1 <= bridge_length:
                truc = truck_weights.popleft()
                bridge.append(truc)
                bridge_weight += truc
                on_the_bridge +=1
            else:
                bridge.append(0)
        else:
            bridge.append(0)
        answer +=1
    return answer

bridge_length, weight, truck_weights = 2,	10	,[7,4,5,6]
solution(bridge_length, weight, truck_weights)