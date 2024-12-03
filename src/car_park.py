from sensor import Sensor
from display import Display
from pathlib import Path
from datetime import datetime  # we'll use this to timestamp entries
import json


class CarPark:
    def __init__(self,
                 location="Unknown",
                 capacity=0,
                 plates=None,
                 sensors=None,
                 displays=None,
                 log_file=Path("log.txt"),
                 config_file=Path("config.txt")
                 ):
        """
                Initialize a CarPark object.

                Parameters:
                location (str): The location of the car park.
                capacity (int): The maximum number of cars the car park can hold.
                plates (list): A list of license plate numbers currently in the car park.
                sensors (list): A list of Sensor objects associated with the car park.
                displays (list): A list of Display objects associated with the car park.
                log_file (Path): The file path where car park logs will be written.
                config_file (Path): The file path to the configuration file for the car park.
                """
        self.location = location
        self.capacity = capacity
        self.plates = plates or []  # List of current license plates in the car park
        self.sensors = sensors or []  # List of Sensor objects
        self.displays = displays or []  # List of Display objects
        self.log_file = log_file if isinstance(log_file, Path) else Path(log_file)
        # create the file if it doesn't exist:
        self.log_file.touch(exist_ok=True)
        self.config_file = config_file if isinstance(config_file, Path) else Path(config_file)

    @property
    def available_bays(self):
        if len(self.plates) > self.capacity:
            return 0
        return self.capacity - len(self.plates)

    def update_displays(self):
        data = {"available_bays": self.available_bays,
                "temperature": 25,
                "message": self.message
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

    # ... inside the CarPark class
    def write_config(self):
        """Save the car park's configuration to the specified config file."""
        config_data = {
            "location": self.location,
            "capacity": self.capacity,
            "log_file": str(self.log_file),
            "plates": self.plates
        }
        with self.config_file.open("w") as f:
            json.dump(config_data, f)

    # ... inside the CarPark class
    @classmethod
    def from_config(cls, config_file=Path("config.json")):
        config_file = config_file if isinstance(config_file, Path) else Path(config_file)
        with config_file.open() as f:
            config = json.load(f)
        return cls(config["location"], config["capacity"], log_file=config["log_file"])

    def __str__(self):
        """Return a string representation of the CarPark object."""
        return f"CarPark at {self.location} with {self.capacity} bays."


if __name__ == '__main__':
    print(repr(CarPark()))
