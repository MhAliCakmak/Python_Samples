class Car:
    Otv = 1.25

    def __init__(self, brand, model, fuel, price):
        self.brand = brand
        self.model = model
        self.fuel = fuel
        self.price = price

    def cost(self):
        return "${}M".format(self.price)

    def new_price(self, much):
        self.price *= much

        return "${}M".format(self.price)

    @classmethod  # I create new class from default class
    def new_car(cls, tnew_name):
        brand, model, fuel, price = tnew_name.split(" ")

        return cls(brand, model, fuel, float(price))

    @staticmethod
    def phone(no):
        phone = no.split(" ")
        return phone


class Bus(Car):  # I use inheritance in here for be easier than

    def __init__(self, luggage, brand, model, fuel, price):
        super().__init__(brand, model, fuel, price)  # Super class should use  for use inheritance
        self.luggage = luggage
        self.Otv = 2.5


class Plane(Car):

    def __init__(self, height, brand, model, fuel, price, weight, car=None):
        super().__init__(brand, model, fuel, price)
        self.height = height
        self.weight = weight
        if Car is None:
            self.car = 0
        else:
            self.car = car

    def car_add(self, cars):
        self.car.append(cars)

    def car_remove(self, cars):
        self.car.remove(cars)

    def car_list(self):

        for i in self.car:
            print(i.brand)

    def pweight(self):
        return f"{self.weight} kg"


Car1 = Car("Alfa_Romeo", "D300", "LPG", 2)  # New car
Car2 = Car("Bugatti", "Veoron", "Water", 3.2)  # New car
Car3 = Car.new_car("Mercedes S5000 Electric 1.5")  # New car
Bus1 = Bus(100, "Ford", "sienta", "Diesel", 0.45)  # New bus
Plane1 = Plane(200, "Anadoljet", "sWi14", "oil", 4.5, 87, [Car1, Car2])

print(f"{Car1.cost()}>>>{Car1.new_price(1.5)}")
print(f"{Car2.cost()}>>>{Car2.new_price(1.2)}")
print(f"{Car3.cost()}>>>{Car3.new_price(1.4)}")
print(f"{Bus1.cost()}>>>{Bus1.new_price(1.4)}")
print(f"{Plane1.cost()}>>>{Plane1.new_price(0.1)}")

print(Plane1.pweight())
print(Plane1.car_list())
print(Plane1.car_add(Car3))
print(Plane1.car_remove(Car2))
print(Plane1.car_list())

print(issubclass(Plane, Car))
print(issubclass(Car, Plane))
print(issubclass(Bus, Car))
print(isinstance(Car1, Car))
