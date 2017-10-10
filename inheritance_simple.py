class vehicle():
    def __init__(self):
        print("This is vehicle class")

class car(vehicle):
        print("This is car class")
    
class motorcycle(vehicle):
    def __init__(self):
        print("This is motorcycle class")

c1=car()
m1=motorcycle()


