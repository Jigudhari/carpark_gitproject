from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display


# Create the car park object
car_park = CarPark(location="Moondalup", capacity=100, log_file="moondalup.txt")

# Create the entry sensor
entry_sensor = EntrySensor(id_=1, is_active=True, car_park=car_park)
car_park.register(entry_sensor)

# Create the exit sensor
exit_sensor = ExitSensor(id_=2, is_active=True, car_park=car_park)
car_park.register(exit_sensor)

# Create the display
display = Display(id_=1, message="Welcome to Moondalup", is_on=True, car_park=car_park)
car_park.register(display)
# Register the sensors and display to the car park

for _ in range(10):
    entry_sensor.detect_vehicle()
for _ in range(2):
    exit_sensor.detect_vehicle()

# for i in range(10):
#     plate = f"CAR{i}"
#     entry_sensor.detect_vehicle()
#
# # Simulate cars leaving
# for i in range(1, 3):
#     plate = f"CAR{i}"
#     exit_sensor.detect_vehicle()
