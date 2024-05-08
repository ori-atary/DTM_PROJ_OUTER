import Classes_2o
import queue

# macro
N = 'N'
W = 'W'
E = 'E'
S = 'S'
left = 'l'
right = 'r'
straight = 's'
directions = {N,W,E,S}
going = {left,right,straight}

# dast:
# Lanes = hold a 3-tuple (from where, where to, lane number), the third is for multiple lanes in the same path
# cars = dictionary of (car_id, Car) to easier access
# lanesQ = dictionary of (lane-tuple,Queue) that holds the queue of car in the lane.
Lanes = []
Cars = {}
LanesQ = {}
Phases = []

# init
for From in directions:
    for To in going:
        Lanes.append((From,To,0))

for lane in Lanes:
     LanesQ[lane] = queue.Queue()

