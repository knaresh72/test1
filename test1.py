import random
import json
import boto3


class ParkingLot:
    def __init__(self, square_footage, spot_width=8, spot_length=12):
        self.spot_size = spot_width * spot_length
        self.num_spots = square_footage // self.spot_size
        self.spots = [None] * self.num_spots
        self.vehicle_map = {}  # Dictionary to map vehicles to spots

    def is_full(self):
        return all(slot is not None for slot in self.spots)

    def park_car(self, car, spot):
        if spot < 0 or spot >= self.num_spots:
            return False  # Invalid spot number
        if self.spots[spot] is None:
            self.spots[spot] = car
            self.vehicle_map[car.license_plate] = spot
            return True
        return False  # Parking spot is occupied

    def map_vehicles_to_spots(self):
        return self.vehicle_map

class Car:

    def __init__(self, license_plate):
        self.license_plate = license_plate

    def __str__(self):
        return f"Car with license plate {self.license_plate}"

def main():
    parking_lot_size = 2000
    parking_lot = ParkingLot(parking_lot_size)

    cars = [Car("ABC1234"), Car("XYZ5678"), Car("DEF4321"), Car("GHI8765")]

    while cars and not parking_lot.is_full():
        car = cars.pop(0)
        spot = random.randint(0, parking_lot.num_spots - 1)

        if parking_lot.park_car(car, spot):
            print(f"{car} parked successfully in spot {spot + 1}")
        else:
            # If the spot is occupied, keep trying to find an empty spot.
            while not parking_lot.park_car(car, spot):
                spot = random.randint(0, parking_lot.num_spots - 1)

    if parking_lot.is_full():
        print("Parking lot is full.")
    else:
        print("All cars parked.")

    # Map vehicles to spots and save it to a JSON file
    vehicle_map = parking_lot.map_vehicles_to_spots()
    with open("vehicle_map.json", "w") as json_file:
        json.dump(vehicle_map, json_file)

    # Uploading the JSON file to an S3 bucket
    s3 = boto3.client('s3')
    s3.upload_file("vehicle_map.json", 'your-s3-bucket-name', 'vehicle_map.json')


if __name__ == "__main__":
    main()
