from models.aerial_vehicle import AerialVehicle


class Dirigible(AerialVehicle):
    """
    Attributes:
        fuel_capacity (int): The capacity of the dirigible's fuel tank in liters.
        fuel_per_hour (int): The rate at which the dirigible consumes fuel per hour in liters.

    Inherits:
        AerialVehicle: An abstract base class representing an aerial vehicle.
    """

    def __init__(
        self,
        weight=None,
        take_of_weight=None,
        manufacturer=None,
        max_speed=None,
        fuel_capacity=None,
        fuel_per_hour=None,
    ):
        super().__init__(weight, take_of_weight, manufacturer, max_speed)
        self.fuel_capacity = fuel_capacity
        self.fuel_per_hour = fuel_per_hour

    __doc__ += AerialVehicle.__doc__

    def get_max_flying_distance(self) -> int:
        flight_time = self.fuel_capacity / self.fuel_per_hour
        return self.max_speed * flight_time
