from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    moving_trucks = deque(([0]*bridge_length))
    waiting_trucks = deque((truck_weights))
    while moving_trucks:
        time += 1
        moving_trucks.popleft()
        if waiting_trucks:
            if sum(moving_trucks) + waiting_trucks[0] <= weight:
                moving_trucks.append(waiting_trucks.popleft())
            else:
                moving_trucks.append(0)
    return time