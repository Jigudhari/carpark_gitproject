class Display:
    def __init__(self,
                 id_,
                 car_park,
                 message="",
                 is_on=False):

        self.id_ = id_
        self.message = message
        self.is_on = is_on
        self.car_park = car_park

    def __str__(self):
        return f"Display{self.id_}: {self.message}"


if __name__ == '__main__':
    print(repr(Display))
