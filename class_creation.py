class car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def display_info(self):
        return f"{self.make} {self.model} {self.year}"
   
   # example 
my_car = car("Toyota", "Camry", 2020)
print(my_car.display_info())