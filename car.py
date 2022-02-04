# def __init__  = constructor
class Car:
    wheels = 4 # class variable promenna, defaultni hodnota

    
    def __init__(self,make,model,year,color):
        self.make = make # instance variable
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        # Self is refering to the object that uses this method
        print("This " +self.model +" is driving")
    
    def stop(self):
        print("This " + self.model + " has stoppped")