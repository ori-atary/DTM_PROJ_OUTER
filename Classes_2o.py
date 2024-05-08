# things to pay attention to:
    # 1. every car should have an ID that is systematically numbered one by one per lane to make it easier to find which ca ris before us
    # 2. we should have a {ID,Vehicle} dict that we can access cars easely though it.
    # 3. we should have the same dict for every Lane,Phase ect.

float TIME_INC = 0.5
accelaration_type = {1,2,3}

def IsFree2Move(id): 
    return True



def init_location(entrence_lane):
    ret = {
        'N' : ('N',-60) ,
        'E' : ('E',-60) ,
        'S' : ('S',-60) ,
        'W' : ('W',-60) ,
        }
    return ret



class Vehicle:
    def __init__(self, type, len, speed, direction[],enter_time,id):
        self.id = id
        self.type = type
        self.len = len
        self.speed = speed
        self.direction = direction
        self.enter_time = enter_time
        self.location = init_location(direction[0])
        
    def move_car(self,next_car_loc):
        if IsFree2Move(self.id) : 
            self.accelarate()
        else:
            self.deccelarate()
        self.change_loc()
        return

    def deccelarate(self):
        return
    

    


# 


class Intersection :
    Phase[]


