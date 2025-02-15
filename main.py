from abc import ABC, abstractmethod

class Driver:
    def __init__(self, driver_id: int, first_name: str, last_name: str, radio_number: str):
        self.driver_id = driver_id
        self.first_name = first_name
        self.last_name = last_name
        self.radio_number = radio_number

    def __str__(self):
        return f"{self.first_name} {self.last_name} (ID: {self.driver_id}, Radio: {self.radio_number})"

class Vehicle(ABC):
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        self.driver = None

    def assign_driver(self, driver: Driver):
        self.driver = driver

    def remove_driver(self):
        self.driver = None

    def update_position(self, x: float, y: float):
        self.x = x
        self.y = y

    @abstractmethod
    def vehicle_info(self) -> str:
        pass

class MiningDumpTruck(Vehicle):
    def __init__(self, x: float, y: float, load_capacity: float, manufacturer: str, model: str):
        super().__init__(x, y)
        self.load_capacity = load_capacity
        self.manufacturer = manufacturer
        self.model = model

    def get_capacity_category(self) -> str:
        pass

    def vehicle_info(self) -> str:
        pass

class NonQuarryDumpTruck(Vehicle):
    def __init__(self, x: float, y: float, cargo: str):
        super().__init__(x, y)
        self.cargo = cargo

    def vehicle_info(self) -> str:
        pass

class ServiceVehicle(Vehicle):
    def __init__(self, x: float, y: float):
        super().__init__(x, y)

    def vehicle_info(self) -> str:
        pass

class Operator:
    def __init__(self, name: str):
        self.name = name

    def send_vehicle_to_repair(self, vehicle: Vehicle):
        pass

    def assign_driver_to_vehicle(self, driver: Driver, vehicle: Vehicle):
        pass

    def remove_driver_from_vehicle(self, vehicle: Vehicle):
        pass
