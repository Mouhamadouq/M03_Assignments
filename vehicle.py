#Super class
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

#automobile class
class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        #call constructor
        Vehicle.__init__(self, vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    #return input
    def __str__(self):
        return "Vehicle type: " + self.vehicle_type + "\nYear: " + self.year + "\nmMake: " + self.make + "\nModel: " + self.model + "\nDoors: " + self.doors + "\nRoof: " + self.roof

if __name__ == "__main__":
    #ask for user input
    year = input("Enter year: ")
    make = input("Enter make: ")
    model = input("Enter model: ")
    doors = input("Enter number of doors (2 or 4): ")
    roof = input("Enter type of roofs (solid or sun): ")

    #Create an object of vehicle
    car = Automobile("Car", year, make, model, doors, roof)
    
    #print outputs
    print("The vehicle details are: ")
    print(car)
