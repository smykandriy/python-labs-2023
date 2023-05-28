from models.aerial_vehicle import AerialVehicle


class Drone(AerialVehicle):
    """
    Attributes:
        battery_capacity (int): The capacity of the drone's battery in ampere-hours.
        battery_charge_per_minute (int): The rate at which the drone's battery charges per minute in ampere-hours.

    Inherits:
        AerialVehicle: An abstract base class representing an aerial vehicle.
    """

    def __init__(
        self,
        weight=None,
        take_of_weight=None,
        manufacturer=None,
        max_speed=None,
        battery_capacity=None,
        battery_charge_per_minute=None,
    ):
        super().__init__(weight, take_of_weight, manufacturer, max_speed)
        self.battery_capacity = battery_capacity
        self.battery_charge_per_minute = battery_charge_per_minute

    __doc__ += AerialVehicle.__doc__

    def get_max_flying_distance(self) -> int:
        flight_time = self.battery_capacity / self.battery_charge_per_minute
        return self.max_speed * flight_time
