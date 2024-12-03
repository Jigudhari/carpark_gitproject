from abc import ABC, abstractmethod
import random


class Sensor(ABC):
    def __init__(self,
                 id_,
                 car_park,
                 is_active=False):
        """
               Initialize a Sensor object.

               Parameters:
               id (str): The unique identifier for the sensor.
               car_park (CarPark): The car park associated with this sensor.
               is_active (bool): Whether the sensor is active. Default is False.
               """
        self.id_ = id_
        self.car_park = car_park
        self.is_active = is_active

    @abstractmethod
    def update_car_park(self, plate):
        pass

    @staticmethod
    def _scan_plate():
        return 'FAKE-' + format(random.randint(0, 999), "03d")

    def detect_vehicle(self):
        plate = self._scan_plate()
        self.update_car_park(plate)


class EntrySensor(Sensor):
    """A sensor specifically for detecting cars entering the car park."""
    def update_car_park(self, plate):
        self.car_park.add_car(plate)
        with open("log.txt", "a") as log_file:
            log_file.write(f"ENTER: {plate}\n")
        print(f"Incoming vehicle detected. Plate:{plate}")


class ExitSensor(Sensor):
    """A sensor specifically for detecting cars exiting the car park."""
    def update_car_park(self, plate):
        if plate in self.car_park.plates:
            self.car_park.remove_car(plate)
            with open("log.txt", "a") as log_file:
                log_file.write(f"EXIT: {plate}\n")
        else:
            print(f"Error: Plate {plate} not found in car park!")
        # self.car_park.remove_car(plate)
        print(f"Outgoing vehicle detected. Plate:{plate}")

    def __str__(self):
        """
                Return a string representation of the Sensor object.

                Returns:
                str: A string containing the sensor's ID and status.
                """

        return f"Sensor {self.id_} {self.is_active}"
