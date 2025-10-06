class engine:
    def start(self):
        print("Engine started")

class wheels:
    def roll(self):
        print("Wheels rolling")

class car(engine, wheels):
    def drive(self):
        print("Car is driving")


mycar = car()
mycar.start()  
mycar.roll()   
mycar.drive()  
        