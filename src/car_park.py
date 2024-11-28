from sensor import Sensor
from display import Display
from pathlib import Path
from datetime import datetime # we'll use this to timestamp entries


class CarPark:
    def __init__(self,
                 location="Unknown",
                 capacity=0,
                 plates=None,
                 sensors=None,
                 displays=None,
                 log_file=Path("log.txt")
                 ):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []  # List of current license plates in the car park
        self.sensors = sensors or []  # List of Sensor objects
        self.displays = displays or []  # List of Display objects
        self.log_file = log_file if isinstance(log_file, Path) else Path(log_file)
        # create the file if it doesn't exist:
        self.log_file.touch(exist_ok=True)

    @property
    def available_bays(self):
        if len(self.plates) > self.capacity:
            return 0
        return self.capacity - len(self.plates)

    def update_displays(self):
        data = {"available_bays": self.available_bays,
                "temperature": 25,
                # "message": self.message
                }
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
        self.plates.append(plate)
        self.update_displays()
        self._log_car_activity(plate, "entered")

    def remove_car(self, plate):
        self.plates.remove(plate)
        self.update_displays()
        self._log_car_activity(plate, "exited")

    # in CarPark class
    def _log_car_activity(self, plate, action):
        with self.log_file.open("a") as f:
            f.write(f"{plate} {action} at {datetime.now():%Y-%m-%d %H:%M:%S}\n")
    def __str__(self):
        """Return a string representation of the CarPark object."""
        return f"CarPark at {self.location} with {self.capacity} bays."


if __name__ == '__main__':
    print(repr(CarPark()))
