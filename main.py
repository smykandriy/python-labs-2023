from managers.aerial_vehicle_manager import AerialVehicleManager
from managers.weapons_set_manager import WeaponsSetManager
from models.dirigible import Dirigible
from models.drone import Drone
from models.helicopter import Helicopter
from models.plane import Plane

aircrafts = AerialVehicleManager()
for _ in range(2):
    aircrafts.add_aircraft(
        Helicopter(
            {"rocket", "bomb", "machine gun"},
            7000,
            13000,
            "Mi",
            130,
            101,
            "Hip",
            2000,
            3800,
            2000,
            200,
            800,
        )
    )
    aircrafts.add_aircraft(Drone({"bomb"}, 10, 25, "DeViro", 70, 300, 3))
    aircrafts.add_aircraft(Dirigible(set(), 70000, 130000, "Zeppelin", 200, 13000, 130))
    aircrafts.add_aircraft(
        Plane({"rocket", "bomb"}, 90000, 120000, "Boeing", 460, 35000, 3500)
    )

for aircraft in aircrafts.aircrafts:
    print(aircraft)

heavy_aircrafts = aircrafts.find_all_heavier_than(50000)
for aircraft in heavy_aircrafts:
    print(aircraft)

deviro_drones = aircrafts.find_all_by_manufacturer("DeViro")
for aircraft in deviro_drones:
    print(aircraft)

# method call logs into file
aircrafts[0].ascend(213)

print(aircrafts.get_max_delivery_weight_list())
print(aircrafts.enumerate_list())
print(aircrafts.get_objects_max_delivery_weight())
print(aircrafts[0].get_attributes_by_type(int))
print(aircrafts.can_take_of_weight(20000))

weapons = WeaponsSetManager(aircrafts)
for weapon in weapons:
    print(weapon)
print(len(weapons))
print(weapons[2])
