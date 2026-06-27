from dataclasses import dataclass

@dataclass
class Car:

    brand: str
    model: str
    price: int

    def get_details(self):
        return f"{self.brand} {self.model} {self.price}$"


car = Car("Toyota", "Fortuner", 5000000)

print(car.get_details())