import queue
from Classes import Lane



# macro
TIME_INC = 0.5.f
CUR_TIME = 0
accelaration_type = {1,2,3} #change later
decelaration_type = {1,2,3} #change later
RED = 0
GREEN = 1
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
# starvationQ = queue which cars will be added to it chronologically so it will knows who's the oldest car

Lanes = []
Cars = {}
starvationQ = queue.Queue()
LanesQ = {}
Phases = []

# init
lane_id = 0
for From in directions:
    for To in going:
        Lanes.append(Lane(From,To,0,lane_id)) # TODO: should add a way to make more than 1 lane
        lane_id += 1

for lane in Lanes:
     LanesQ[lane] = queue.Queue()

