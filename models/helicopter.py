from models.aerial_vehicle import AerialVehicle


class Helicopter(AerialVehicle):
    """
    A class representing a helicopter.

    Attributes:
        TAKE_OFF_ALTITUDE (int): The altitude gained by the helicopter during takeoff.
        id (int): The unique identifier of the helicopter.
        model (str): The model of the helicopter.
        current_altitude (int): The current altitude of the helicopter in meters.
        max_altitude (int): The maximum altitude the helicopter can reach in meters.
        fuel_capacity (int): The maximum amount of fuel the helicopter can hold in liters.
        fuel_per_hour (int): The rate at which the dirigible consumes fuel per hour in liters.
        current_fuel (int): The current amount of fuel in the helicopter's tank in liters.

    Methods:
        take_off(self):
            Increases the current altitude of the helicopter by the TAKE_OFF_ALTITUDE attribute.
            If the new altitude would exceed the maximum altitude of the helicopter,
            sets the current altitude to the maximum altitude.

        ascend(self, altitude):
            Increases the current altitude of the helicopter by the specified amount.
            Raises a ValueError if the altitude argument is negative.
            If the new altitude would exceed the maximum altitude of the helicopter,
            sets the current altitude to the maximum altitude.

        descend(self, altitude):
            Descends the helicopter by a specified altitude.
            Raises a ValueError if the altitude is less than zero.
            If the new altitude would go below zero, sets the current altitude to zero.

        refuel(self, fuel):
            Refuels the helicopter by a specified amount of fuel.
            Raises a ValueError if the fuel is less than zero.
            If the new fuel amount would exceed the fuel capacity of the helicopter,
            sets the current fuel to the fuel capacity.
    """

    TAKE_OFF_ALTITUDE = 100
    __instance = None

    def __init__(
        self,
        weight=None,
        take_of_weight=None,
        manufacturer=None,
        max_speed=None,
        id=102,
        model=None,
        current_altitude=None,
        max_altitude=None,
        fuel_capacity=None,
        fuel_per_hour=None,
        current_fuel=None,
    ):
        super().__init__(weight, take_of_weight, manufacturer, max_speed)
        self.id = id
        self.model = model
        self.current_altitude = current_altitude
        self.max_altitude = max_altitude
        self.fuel_capacity = fuel_capacity
        self.fuel_per_hour = fuel_per_hour
        self.current_fuel = current_fuel

    __doc__ += AerialVehicle.__doc__

    def __str__(self):
        base_str = super().__str__()
        attrs_dict = self.__dict__
        attrs = [f"{key.split(sep='_')[-1]}: {attrs_dict[key]}" for key in attrs_dict]
        return f"{base_str}, {' '.join(attrs)}"

    def __eq__(self, other):
        return self.__instance == other.__instance

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def value_error(self, value_name):
        raise ValueError(
            f"Invalid {value_name} value: {value_name} cannot be negative."
        )

    def take_off(self):
        """
        Increases the current altitude of the helicopter by the TAKE_OFF_ALTITUDE attribute.

        If the new altitude would exceed the maximum altitude of the helicopter,
        sets the current altitude to the maximum altitude.
        """
        if self.current_altitude + self.TAKE_OFF_ALTITUDE > self.max_altitude:
            self.current_altitude = self.max_altitude
            return
        self.current_altitude += self.TAKE_OFF_ALTITUDE

    def ascend(self, altitude):
        """
        Increases the current altitude of the helicopter by the specified amount.

        Args:
            altitude (int): The amount to increase the altitude in meters.

        Raises:
            ValueError: If the altitude argument is negative.

        If the new altitude would exceed the maximum altitude of the helicopter,
        sets the current altitude to the maximum altitude.
        """
        if altitude < 0:
            self.value_error("altitude")
        if self.current_altitude + altitude > self.max_altitude:
            self.current_altitude = self.max_altitude
            return
        self.current_altitude += altitude

    def descend(self, altitude):
        """
        Descends the helicopter by a specified altitude.

        Args:
            altitude (int or float): The amount by which to descend the helicopter.

        Raises:
            ValueError: If the altitude is less than zero.

        Returns:
            None
        """
        if altitude < 0:
            self.value_error("altitude")
        if self.current_altitude - altitude < 0:
            self.current_altitude = 0
            return
        self.current_altitude -= altitude

    def refuel(self, fuel):
        """
        Refuels the helicopter by a specified amount of fuel.

        Args:
            fuel (int or float): The amount of fuel to add to the helicopter.

        Raises:
            ValueError: If the fuel is less than zero.

        Returns:
            None
        """
        if fuel < 0:
            self.value_error("fuel")
        if self.current_fuel + fuel > self.fuel_capacity:
            self.current_fuel = self.fuel_capacity
            return
        self.current_fuel += fuel

    def get_max_flying_distance(self) -> int:
        flight_time = self.fuel_capacity / self.fuel_per_hour
        return self.max_speed * flight_time
