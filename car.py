class Car():
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        log_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return log_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading"""
        self.odometer_reading += miles




class Battery():
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size = 70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kwh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        rango = ''
        if self.battery_size == 70:
            rango = 240
        elif self.battery_size == 85:
            rango = 270

        message = "This car can go approximately " + str(rango)
        message += " miles on a full charge."
        print(message)

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    """
    The __init__() method takes in the information required to make a Car
    instance.
    """
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        """
        The super() function is a special function that helps Python make
        connections between the parent and child class. This line tells Python to
        call the __init__() method from ElectricCar’s parent class, which gives an
        ElectricCar instance all the attributes of its parent class. The name super
        comes from a convention of calling the parent class a superclass and the
        child class a subclass.
        """
        super().__init__(make, model, year)
        self.battery = Battery()