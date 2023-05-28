class AerialVehicleManager:
    """
    Attributes:
        aircrafts (list): A list of aerial vehicles managed by the manager.
    """

    def __init__(self):
        self.aircrafts = []

    def __len__(self):
        return len(self.aircrafts)

    def __getitem__(self, index):
        return self.aircrafts[index]

    def __iter__(self):
        return iter(self.aircrafts)

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

    def get_max_delivery_weight_list(self):
        return [aircraft.get_max_delivery_weight() for aircraft in self.aircrafts]

    def enumerate_list(self):
        return list(enumerate(self.aircrafts))

    def get_objects_max_delivery_weight(self):
        delivery_weight_list = self.get_max_delivery_weight_list()
        return list(zip(self.aircrafts, delivery_weight_list))

    def can_take_of_weight(self, weight):
        return {
            "all": all(
                aircraft.take_of_weight >= weight for aircraft in self.aircrafts
            ),
            "any": any(
                aircraft.take_of_weight >= weight for aircraft in self.aircrafts
            ),
        }
