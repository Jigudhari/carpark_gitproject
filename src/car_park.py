from sensor import Sensor
from display import Display


class CarPark:
    def __init__(self,
                 location="Unknown",
                 capacity=0,
                 plates=None,
                 sensors=None,
                 displays=None
                 ):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []  # List of current license plates in the car park
        self.sensors = sensors or []  # List of Sensor objects
        self.displays = displays or []  # List of Display objects

    @property
    def available_bays(self):
        if len(self.plates) > self.capacity:
            return 0
        return self.capacity - len(self.plates)

    def update_displays(self):
        data = {"available_bays": self.available_bays,
                "temperature": 25}
        for display in self.displays:
            display.update(data)

    def register(self, component):
        """
               Register a component (Sensor or Display) to the car park.

               Parameters:
               component (Sensor or Display): The component to register.

               Raises:
               TypeError: If the component is not a Sensor or Display.
               """
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a Sensor or Display.")
        if isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)

    def add_car(self, plate):
        self.plates.apppend(plate)
        self.update_displays()

    def remove_car(self, plate):
        self.plates.remove(plate)
        self.update_displays()


    def __str__(self):
        """Return a string representation of the CarPark object."""
        return f"CarPark at {self.location} with {self.capacity} bays."


if __name__ == '__main__':
    print(repr(CarPark()))
