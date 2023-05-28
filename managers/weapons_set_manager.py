from managers.aerial_vehicle_manager import AerialVehicleManager


class WeaponsSetManager:
    def __init__(self, regular_manager: AerialVehicleManager):
        self.regular_manager = regular_manager

    def __iter__(self):
        for aircraft in self.regular_manager:
            yield from aircraft.weapons

    def __len__(self):
        return sum(len(aircraft.weapons) for aircraft in self.regular_manager)

    def __getitem__(self, index):
        for aircraft in self.regular_manager:
            if index < len(aircraft.weapons):
                return list(aircraft.weapons)[index]
            index -= len(aircraft.weapons)
        raise IndexError("Index out of range")

    def __next__(self):
        for aircraft in self.regular_manager:
            for weapon in aircraft.weapons:
                yield weapon
