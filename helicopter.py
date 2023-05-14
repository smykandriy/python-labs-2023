class Helicopter:
    """
    A class representing a helicopter.

    Attributes:
        TAKE_OFF_ALTITUDE (int): The altitude gained by the helicopter during takeoff.
        __id (int): The unique identifier of the helicopter.
        __model (str): The model of the helicopter.
        __current_altitude (int): The current altitude of the helicopter in meters.
        __max_altitude (int): The maximum altitude the helicopter can reach in meters.
        __fuel_capacity (float): The maximum amount of fuel the helicopter can hold in liters.
        __current_fuel (float): The current amount of fuel in the helicopter's tank in liters.

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
    instance = None

    def __init__(
        self,
        __id=102,
        __model=None,
        __current_altitude=None,
        __max_altitude=None,
        __fuel_capacity=None,
        __current_fuel=None,
    ):
        """
        Initializes a Helicopter object.

        Args:
            __id (int): The unique identifier of the helicopter.
            __model (str): The model of the helicopter.
            __current_altitude (int): The current altitude of the helicopter in meters.
            __max_altitude (int): The maximum altitude the helicopter can reach in meters.
            __fuel_capacity (float): The maximum amount of fuel the helicopter can hold in liters.
            __current_fuel (float): The current amount of fuel in the helicopter's tank in liters.
        """
        self.__id = __id
        self.__model = __model
        self.__current_altitude = __current_altitude
        self.__max_altitude = __max_altitude
        self.__fuel_capacity = __fuel_capacity
        self.__current_fuel = __current_fuel

    def __str__(self):
        """
        Returns a string representation of the helicopter.

        Returns:
        str: A string that includes the helicopter ID, model, maximum altitude, current altitude, fuel capacity,
        and current fuel level.
        """
        attrs = [f"{key.split(sep='_')[-1]}: {self.__dict__[key]}" for key in self.__dict__]
        return f"{self.__class__.__name__}({', '.join(attrs)})"

    @staticmethod
    def get_instance():
        if Helicopter.instance is None:
            Helicopter.instance = Helicopter()
        return Helicopter.instance

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        self.__model = value

    @property
    def current_altitude(self):
        return self.__current_altitude

    @current_altitude.setter
    def current_altitude(self, value):
        self.__current_altitude = value

    @property
    def max_altitude(self):
        return self.__max_altitude

    @max_altitude.setter
    def max_altitude(self, value):
        self.__max_altitude = value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, value):
        self.__fuel_capacity = value

    @property
    def current_fuel(self):
        return self.__current_fuel

    @current_fuel.setter
    def current_fuel(self, value):
        self.__current_fuel = value

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
        if self.__current_altitude + self.TAKE_OFF_ALTITUDE > self.__max_altitude:
            self.__current_altitude = self.__max_altitude
            return
        self.__current_altitude += self.TAKE_OFF_ALTITUDE

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
        if self.__current_altitude + altitude > self.__max_altitude:
            self.__current_altitude = self.__max_altitude
            return
        self.__current_altitude += altitude

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
        if self.__current_altitude - altitude < 0:
            self.__current_altitude = 0
            return
        self.__current_altitude -= altitude

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
        if self.__current_fuel + fuel > self.__fuel_capacity:
            self.__current_fuel = self.__fuel_capacity
            return
        self.__current_fuel += fuel


if __name__ == "__main__":
    helicopters = [
        Helicopter(),
        Helicopter(103, "Apache", 1200, 3000, 500, 430),
        Helicopter.get_instance(),
        Helicopter.get_instance(),
    ]

    for _ in helicopters:
        print(_)
