# Prioritization of attribute search


class Warehouse:
    # class data attributes
    purpose = "storage"
    location = "west"
    __size = "unknown"

    def get_size(self):
        return self.__size

    # def __init__(self, location):
    #     self.location = location


west_house = Warehouse()

east_house = Warehouse()
east_house.location = "east"

print(east_house.purpose + " " + east_house.location)
print(west_house.purpose + " " + west_house.location)
print(Warehouse.purpose + " " + Warehouse.location)

print(west_house.get_size())
