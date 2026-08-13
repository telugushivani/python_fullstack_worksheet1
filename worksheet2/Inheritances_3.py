class Vehicle:
    def start(self):
        print("Vehicle Started")
    def stop(self):    
        print("Vehical Stopped")
class car(Vehicle):
    def  drive(self):
        print("Car Driving")
d=car()
d.start()
d.drive()
d.stop()
