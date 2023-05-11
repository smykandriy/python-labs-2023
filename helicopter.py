class Helicopter:
    TAKE_OFF_ALTITUDE = 100

    def __init__(self, id, model, current_altitude, max_altitude, fuel_capacity, current_fuel):
        self.id = id
        self.model = model
        self.current_altitude = current_altitude
        self.max_altitude = max_altitude
        self.fuel_capacity = fuel_capacity
        self.current_fuel = current_fuel

    def __str__(self):
        return f"""
        Helicopter {self.id} ({self.model})
        Max Altitude: {self.max_altitude}
        Current Altitude: {self.current_altitude}
        Fuel Capacity: {self.fuel_capacity}
        Current fuel: {self.current_fuel}"""

    def take_off(self):
        if self.current_altitude + self.TAKE_OFF_ALTITUDE > self.max_altitude:
            self.current_altitude = self.max_altitude
            return
        self.current_altitude += self.TAKE_OFF_ALTITUDE

    def ascend(self, altitude):
        if altitude < 0:
            raise ValueError("Invalid altitude value: altitude cannot be negative.")
        if self.current_altitude + altitude > self.max_altitude:
            self.current_altitude = self.max_altitude
            return
        self.current_altitude += altitude

    def descend(self, altitude):
        if altitude < 0:
            raise ValueError("Invalid altitude value: altitude cannot be negative.")
        if self.current_altitude - altitude < 0:
            self.current_altitude = 0
            return
        self.current_altitude -= altitude

    def refuel(self, fuel):
        if fuel < 0:
            raise ValueError("Invalid fuel value: fuel cannot be negative.")
        if self.current_fuel + fuel > self.fuel_capacity:
            self.current_fuel = self.fuel_capacity
            return
        self.current_fuel += fuel
