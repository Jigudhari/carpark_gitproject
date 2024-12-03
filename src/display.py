class Display:
    def __init__(self,
                 id_,
                 car_park,
                 message="",
                 is_on=False):
        """
                Initialize a Display object.

                Parameters:
                id (str): The unique identifier for the display.
                car_park (CarPark): The car park associated with this display.
                message (str): The message to be displayed. Default is an empty string.
                is_on (bool): Whether the display is turned on. Default is False.
                """

        self.id_ = id_
        self.message = message
        self.is_on = is_on
        self.car_park = car_park

    # @staticmethod
    def update(self, data):
        for key, value in data.items():
            print(f"{key}: {value}")
            if "message" in data:
                self.message = data['message']

    def __str__(self):
        """
                Return a string representation of the Display object.

                Returns:
                str: A string containing the display's ID and message.
                """
        return f"Display{self.id_}: {self.message}"


if __name__ == '__main__':
    print(repr(Display))
