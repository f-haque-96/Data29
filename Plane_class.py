class Plane:
    def __init__(self, year, make, speed):
        self.__year_model = year
        self.__make = make
        self.__speed = 0

    def set_year_model(self, year):
        self.__year_model = year

    def set_make(self, make):
        self.__make = make

    def set_speed(self, speed):
        self.__speed = 0

    def get_year_model(self):
        return self.__year_model

    def get_make(self):
        return self.__make

    def get_speed(self):
        return self.__speed

    #methods
    def accelerate(self):
        self.__speed +=5

    def altitude(self):
        self.__speed +=5

    def get_speed(self):
        return self.__speed

def main():

    year = input('Enter the plane year: ')
    make = input('Enter the plane make: ')
    speed = 0

    mycar = Car(year, make, speed)

    #Accelerate 5 times
    mycar.accelerate()
    print('The current speed is: ', mycar.get_speed())
    mycar.accelerate()
    print('The current speed is: ', mycar.get_speed())
    mycar.accelerate()
    print('The current speed is: ', mycar.get_speed())
    mycar.accelerate()
    print('The current speed is: ', mycar.get_speed())
    mycar.accelerate()
    print('The current speed is: ', mycar.get_speed())

    #Altitude 5 times
    mycar.altitude()
    print('The current altitude: ', mycar.get_speed())
    mycar.altitude()
    print('The current altitude: ', mycar.get_speed())
    mycar.altitude()
    print('The current altitude: ', mycar.get_speed())
    mycar.altitude()
    print('The current altitude: ', mycar.get_speed())
    mycar.altitude()
    print('The current altitude: ', mycar.get_speed())

#Call the main function
main()
