# things to pay attention to:
    # 1. every car should have an ID that is systematically numbered one by one per lane to make it easier to find which ca ris before us
    # 2. we should have a {ID,Vehicle} dict that we can access cars easely though it.
    # 3. we should have the same dict for every Lane,Phase ect.
    # 4. we neede to add path as where to and from the car is coming, then we can decide the lane it should go to. 
    # 5. path == {from,to} 

from data_structurs import *

TIME_INC = 0.5.f
accelaration_type = {1,2,3}
decelaration_type = {1,2,3}

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

def calc_lane(path):
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


class Vehicle:
    def __init__(self, type, len, speed, path,enter_time,id):
        self.id = id
        self.type = type
        self.len = len
        self.speed = speed
        self.path = path
        self.lane = calc_lane(path)
        self.enter_time = enter_time
        self.location = init_location(path[0])
        self.queue = LanesQ[self.lane]

        Cars[id] = self
        LaneQ[self.lane].put(self.id)
        
    def move_car(self,next_car_loc):
        if IsFree2Move(self) : 
            self.accelarate()
        else:
            self.decelarate()
        self.change_loc()
        return

    def decelarate(self):
        self.speed -= TIME_INC*decelaration_type[self.type]
        self.speed = max(0,self.speed)
        return
    
    def accelarate(self):
        self.speed += TIME_INC*accelaration_type[self.type]
        return

    def change_loc(self):
        if self.location[1] - (self.speed*TIME_INC) < 0 :
            # it means that car is entering critical area
            x=1 #just here as placeholder to avoid error
        else:
            self.location -= self.speed*TIME_INC
        return


    


# 


class Intersection :
    Phase[]


