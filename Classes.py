# things to pay attention to:
    # 1. every car should have an ID that is systematically numbered one by one per lane to make it easier to find which ca ris before us
    # 2. we should have a {ID,Vehicle} dict that we can access cars easely though it.
    # 3. we should have the same dict for every Lane,Phase ect.
    # 4. we neede to add path as where to and from the car is coming, then we can decide the lane it should go to. 
    # 5. path == {from,to} 
    # 6. pay attention to update every car added to any lane to Lane->Phase->Intersection

from data_structurs import *
from functions import *



class Vehicle:
    def __init__(self, type, len, speed, path,enter_time,id):
        self.id = id
        self.type = type
        self.len = len
        self.speed = speed
        self.path = path
        self.lane = calcLane(path)
        self.enter_time = enter_time
        self.location = init_location(path[0])
        self.queue = LanesQ[self.lane]

        Cars[id] = self
        LanesQ[self.lane].put(self.id)
        
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
    
    def wait_time(self):
        return CUR_TIME - self.enter_time


class Lane :
    def __init__(self,From,To,num,id):
        self.id = id
        self.source = From
        self.dest = To
        self.num = num
        self.q = queue.Queue()
        self.tuple = (From,To,num)
        self.cumulative_time = 0
    
    def calc_cum_time(self):
        cumulative_time = 0
        for car in self.q:
            cumulative_time += car.wait_time()
        self.cumulative_time = cumulative_time
        return cumulative_time
    
    def change_status(self,status):
        self.status = status

class Phase : 
    def __init__(self,lanes,id):
        self.lanes = lanes
        self.id = id
        self.cumulative_time = 0
        self.status = RED
    
    def calc_cum_time(self):
        cumulative_time = 0
        for lane in self.lanes:
            cumulative_time += lane.calc_cum_time()
        self.cumulative_time = cumulative_time
        return cumulative_time
    
    def change_status(self,status):
        self.status = status
        for lane in self.lanes:
            lane.change_status(status)

    







class Intersection :
    def __init__(self, Phase):
        self.car = 0

