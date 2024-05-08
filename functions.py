from data_structurs import *
from Classes import *





def isFirst(car):
    return car.queue[0] == car

def greenLight(car):
    return True
    

# returns the car instance of the car standing before this one
def nextCar(car):
    if isFirst(car) :
        return 0
    for i in range(car.queue.qsize()) :
        if car.queue[i] == car :
            return car.queue[i-1]


def IsFree2Move(car): 
    # right now we are implementing simple solution: if the car has 3m or more, it free to move.
    # maybe later we can try something more sofisticated.
    if isFirst(car) and greenLight(car) : 
        return True
    next = nextCar(car)
    return True if next.location - next.len - car.location > 3 else False

def calcLane(path):
    lanes = []
    for i in range(3):
        if (path[0],path[1],i) in Lanes : 
            lanes.append((path[0],path[1],i))
    if len(lanes) == 1 :
        return lanes[0]
    # else choose the least busy lane
    min_size = 1000
    choosing = -1
    for lane in lanes:
        if min_size > LanesQ[lane].qsize():
            min_size = LanesQ[lane].qsize()
            choosing = lane
    return choosing 

def init_location(entrance_lane):
    ret = {
        N : (N,-60) ,
        E : (E,-60) ,
        S : (S,-60) ,
        W : (W,-60) ,
        }
    return ret

