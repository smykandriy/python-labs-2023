from exceptions.exceptions import NegativeAttributeValue
from models.aerial_vehicle import AerialVehicle
from decorators.decorators import (
    log_method_calls,
    validate_method_naming_convention,
    logged,
)


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
        weapons: set,
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
        super().__init__(weapons, weight, take_of_weight, manufacturer, max_speed)
        self.id = id
        self.model = model
        self.current_altitude = current_altitude
        self.max_altitude = max_altitude
        self.fuel_capacity = fuel_capacity
        self.fuel_per_hour = fuel_per_hour
        self.current_fuel = current_fuel

    __doc__ += AerialVehicle.__doc__

    @validate_method_naming_convention
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

    @log_method_calls("method_calls.log")
    @logged(NegativeAttributeValue, "file")
    def ascend(self, altitude):
        """
        Increases the current altitude of the helicopter by the specified amount.

        Args:
            altitude (int): The amount to increase the altitude in meters.

        Raises:
            NegativeAttributeValue: If the altitude is less than zero.

        If the new altitude would exceed the maximum altitude of the helicopter,
        sets the current altitude to the maximum altitude.
        """
        if altitude < 0:
            raise NegativeAttributeValue("altitude")
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
            NegativeAttributeValue: If the altitude is less than zero.

        Returns:
            None
        """
        if altitude < 0:
            raise NegativeAttributeValue("altitude")
        if self.current_altitude - altitude < 0:
            self.current_altitude = 0
            return
        self.current_altitude -= altitude

    @logged(NegativeAttributeValue, "console")
    def refuel(self, fuel):
        """
        Refuels the helicopter by a specified amount of fuel.

        Args:
            fuel (int or float): The amount of fuel to add to the helicopter.

        Raises:
            NegativeAttributeValue: If the fuel is less than zero.

        Returns:
            None
        """
        if fuel < 0:
            raise NegativeAttributeValue("fuel")
        if self.current_fuel + fuel > self.fuel_capacity:
            self.current_fuel = self.fuel_capacity
            return
        self.current_fuel += fuel

    def get_max_flying_distance(self) -> int:
        flight_time = self.fuel_capacity / self.fuel_per_hour
        return self.max_speed * flight_time
