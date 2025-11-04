# parent

class Factory:
    def __init__(self):
        pass

    def make_vehicle(self):
        print("I am making a general vehicle")


# class Child_class_name(parent_Class_name)
class CarFactory(Factory):
    def __init__(self):
        pass

    # manufacture cars
    def make_cars(self):
        print("I am manufacturing only CARS")

    def make_vehicle(self):
        print("I am changing my grandparents class to my own")

new_car_factory = CarFactory()
# self property
new_car_factory.make_cars()

# parent property
new_car_factory.make_vehicle()




# class Child_class_name(parent_Class_name)
class BikeFactory(Factory):
    def __init__(self):
        pass

    def make_bike(self):
        print("I am manufacturing only bikes")

    def make_vehicle(self):
        print("I am changing my grandparent class to my own")



     
new_bike_factory = BikeFactory()
# self property
new_bike_factory.make_bike()

# parent property
new_bike_factory.make_vehicle()   
