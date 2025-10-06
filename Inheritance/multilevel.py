class vehicle:
    def start(self):
        print("Vehicle is Started")

class car(vehicle):
    def drive(self):
        print("Car is driving")

class electric(car):
    def charge(self):
        print("car is charging")

ecar=electric()
ecar.start()
ecar.drive()
ecar.charge()