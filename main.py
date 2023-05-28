from managers.aerial_vehicle_manager import AerialVehicleManager
from models.dirigible import Dirigible
from models.drone import Drone
from models.helicopter import Helicopter
from models.plane import Plane

aircrafts = AerialVehicleManager()
for _ in range(2):
    aircrafts.add_aircraft(
        Helicopter(7000, 13000, "Mi", 70, 101, "Hip", 2000, 3800, 2000, 200, 800)
    )
    aircrafts.add_aircraft(Drone(10, 25, "DeViro", 70, 300, 3))
    aircrafts.add_aircraft(Dirigible(70000, 130000, "Zeppelin", 200, 13000, 130))
    aircrafts.add_aircraft(Plane(90000, 120000, "Boeing", 460, 35000, 3500))

for aircraft in aircrafts.aircrafts:
    print(aircraft)

heavy_aircrafts = aircrafts.find_all_heavier_than(50000)
for aircraft in heavy_aircrafts:
    print(aircraft)

deviro_drones = aircrafts.find_all_by_manufacturer("DeViro")
for aircraft in deviro_drones:
    print(aircraft)
