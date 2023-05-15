from helicopter import Helicopter

helicopters = [
    Helicopter(),
    Helicopter(103, "Apache", 1200, 3000, 500, 430),
    Helicopter.get_instance(),
    Helicopter.get_instance(),
]

for _ in helicopters:
    print(_)
