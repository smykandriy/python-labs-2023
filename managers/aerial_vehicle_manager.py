class AerialVehicleManager:
    """
    Attributes:
        aircrafts (list): A list of aerial vehicles managed by the manager.
    """
    def __init__(self):
        self.aircrafts = []

    def add_aircraft(self, aircraft):
        """
        Add an aerial vehicle to the manager.

        Args:
            aircraft (AerialVehicle): The aerial vehicle to add.

        Returns:
            None
        """
        self.aircrafts.append(aircraft)

    def find_all_heavier_than(self, weight):
        """
        Find all aerial vehicles in the manager that are heavier than a specified weight.

        Args:
            weight (int): The weight threshold to compare against.

        Returns:
            list: A list of aerial vehicles that are heavier than the specified weight.
        """
        return list(filter(lambda aircraft: aircraft.weight > weight, self.aircrafts))

    def find_all_by_manufacturer(self, manufacturer):
        """
        Find all aerial vehicles in the manager that are manufactured by a specified manufacturer.

        Args:
            manufacturer (str): The manufacturer to search for.

        Returns:
            list: A list of aerial vehicles that are manufactured by the specified manufacturer.
        """
        return list(
            filter(
                lambda aircraft: aircraft.manufacturer == manufacturer, self.aircrafts
            )
        )
