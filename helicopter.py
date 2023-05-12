class Helicopter:
    TAKE_OFF_ALTITUDE = 100

    def __init__(self, id, model, current_altitude, max_altitude, fuel_capacity, current_fuel):
        """
        Creates a new instance of a Helicopter.

        Parameters:
        id (int): The unique identifier of the helicopter.
        model (str): The model of the helicopter.
        current_altitude (float): The current altitude of the helicopter in feet.
        max_altitude (float): The maximum altitude that the helicopter can reach in feet.
        fuel_capacity (float): The maximum amount of fuel that the helicopter can carry in gallons.
        current_fuel (float): The current amount of fuel that the helicopter has in gallons.
        """
        self.id = id
        self.model = model
        self.current_altitude = current_altitude
        self.max_altitude = max_altitude
        self.fuel_capacity = fuel_capacity
        self.current_fuel = current_fuel

    def __str__(self):
        """
        Returns a string representation of the helicopter.

        Returns:
        str: A string that includes the helicopter ID, model, maximum altitude, current altitude, fuel capacity,
        and current fuel level.
        """
        attrs = {
            'id': self.id,
            'model': self.model,
            'max_altitude': self.max_altitude,
            'current_altitude': self.current_altitude,
            'fuel_capacity': self.fuel_capacity,
            'current_fuel': self.current_fuel
        }
        docstring = [f"{key.capitalize()}: {attrs[key]}" for key in attrs]
        return f"{self.__class__.__name__}({', '.join(docstring)})"

    def value_error(self, value_name):
        raise ValueError(f"Invalid {value_name} value: {value_name} cannot be negative.")

    def take_off(self):
        if self.current_altitude + self.TAKE_OFF_ALTITUDE > self.max_altitude:
            self.current_altitude = self.max_altitude
            return
        self.current_altitude += self.TAKE_OFF_ALTITUDE

    def ascend(self, altitude):
        if altitude < 0:
            self.value_error("altitude")
        if self.current_altitude + altitude > self.max_altitude:
            self.current_altitude = self.max_altitude
            return
        self.current_altitude += altitude

    def descend(self, altitude):
        if altitude < 0:
            self.value_error("altitude")
        if self.current_altitude - altitude < 0:
            self.current_altitude = 0
            return
        self.current_altitude -= altitude

    def refuel(self, fuel):
        if fuel < 0:
            self.value_error("fuel")
        if self.current_fuel + fuel > self.fuel_capacity:
            self.current_fuel = self.fuel_capacity
            return
        self.current_fuel += fuel
