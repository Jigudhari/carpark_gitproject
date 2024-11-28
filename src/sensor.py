from abc import ABC, abstractmethod
import random


class Sensor(ABC):
    def __init__(self,
                 id_,
                 car_park,
                 is_active=False):
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
    def update_car_park(self, plate):
        self.car_park.add_car(plate)
        print(f"Incoming vehicle detected. Plate:{plate}")


class ExitSensor(Sensor):
    def update_car_park(self, plate):
        if plate in self.car_park.plates:
            self.car_park.remove_car(plate)
        else:
            print(f"Error: Plate {plate} not found in car park!")
        # self.car_park.remove_car(plate)
        print(f"Outgoing vehicle detected. Plate:{plate}")

    def __str__(self):

        return f"Sensor {self.id_} {self.is_active}"
