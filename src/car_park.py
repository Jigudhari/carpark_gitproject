class CarPark:
    def __init__(self,
                 location="Unknown",
                 capacity=0,
                 plates=None,
                 sensors=None,
                 displays=None
                 ):
        if plates is None:
            plates = []
        self.location = location
        self.capacity = capacity
        self.plates = plates or []  # List of current license plates in the car park
        self.sensors = sensors or []  # List of Sensor objects
        self.displays = displays or []  # List of Display objects

    def __str__(self):
        """Return a string representation of the CarPark object."""
        return f"CarPark at {self.location} with {self.capacity} bays."


if __name__ == '__main__':
    print(repr(CarPark()))
