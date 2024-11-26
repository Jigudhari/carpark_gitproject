class Sensor:
    def __init__(self,
                 id_,
                 car_park,
                 is_active=False):
        self.id_ = id_
        self.car_park = car_park
        self.is_active = is_active

    def __str__(self):

        return f"Sensor {self.id_} {self.is_active}"


class EntrySensor(Sensor):
    pass


class ExitSensor(Sensor):
    pass
