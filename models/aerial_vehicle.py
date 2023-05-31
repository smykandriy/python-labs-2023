from abc import ABC, abstractmethod


class AerialVehicle(ABC):
    """
    An abstract base class representing an aerial vehicle.

    Attributes:
        weight (int): The weight of the aerial vehicle in kilograms.
        take_of_weight (int): The maximum take-off weight of the aerial vehicle in kilograms.
        manufacturer (str): The manufacturer of the aerial vehicle.
        max_speed (int): The maximum speed of the aerial vehicle in kilometers per hour.
    """

    def __init__(
        self,
        weapons: set,
        weight=None,
        take_of_weight=None,
        manufacturer=None,
        max_speed=None,
    ):
        self.weapons = weapons
        self.weight = weight
        self.take_of_weight = take_of_weight
        self.manufacturer = manufacturer
        self.max_speed = max_speed

    def __repr__(self):
        attrs_dict = self.__dict__
        attrs = [f"{key}: {attrs_dict[key]}" for key in attrs_dict]
        return f"{self.__class__.__name__}({', '.join(attrs)})"

    def __iter__(self):
        return iter(self.weapons)

    def __str__(self):
        return f"{self.__class__.__name__}: {self.manufacturer}, {self.weight}"

    @abstractmethod
    def get_max_flying_distance(self) -> int:
        """
        Returns the maximum flying distance of the aerial vehicle.

        Returns:
            int: The maximum flying distance of the aerial vehicle in kilometers.
        """

    def get_max_delivery_weight(self) -> int:
        """
        Returns the maximum delivery weight of the aerial vehicle.

        Returns:
            int: The maximum delivery weight of the aerial vehicle in kilograms.
        """
        return self.take_of_weight - self.weight

    def get_attributes_by_type(self, data_type):
        """
        Retrieve attributes from the object by the specified data type.

        Args:
            data_type (type): The data type to filter the attributes by.

        Returns:
            dict: A dictionary containing attribute names as keys and their corresponding values,
                  for attributes whose values match the specified data type.
        """
        return {
            key: value
            for key, value in self.__dict__.items()
            if isinstance(value, data_type)
        }
