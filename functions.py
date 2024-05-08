from data_structurs import *
from Classes import *


def isFirst(car):
    return car.queue[0] == car

def greenLight(car):
    return car.lane.status
    

# returns the car instance of the car standing before this one,
# # 0 if there aren't any
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
    for lane in Lanes:
        if lane.source == path[0] and lane.dest == path[1]:
            lanes.append(lane)
    if len(lanes) == 1 :
        return lanes[0]
    # else choose the least busy lane
    min_size = 1000
    ret = 0
    for lane in lanes:
        if min_size > lane.q.qsize():
            min_size = lane.q.qsize()
            ret = lane
    return ret
    
def calcCarID(lane):
    return lane.id*10000 + lane.car_counter


def init_location(entrance_lane):
    ret = {
        N : (N,-60) ,
        E : (E,-60) ,
        S : (S,-60) ,
        W : (W,-60) ,
        }
    return ret


# updates: Cars,LaneQ,starvationQ,Lane.car_counter
def enter_new_car( type, len, speed, path):
    lane = calcLane(path)
    lane.car_counter += 1
    id = calcCarID(lane)
    car = Vehicle(type, len, speed, path,CUR_TIME,id)
    Cars[car.id] = car
    starvationQ.put(car)
    LanesQ[lane].put(car)
    return



def check_cars_to_enter(table):
    return
