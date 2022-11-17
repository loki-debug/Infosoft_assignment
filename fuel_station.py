class FuelStation:
    
    def __init__(self, diesel: int, petrol: int, electric:int):
        self.diesel: int = diesel
        self.petrol: int = petrol
        self.electric: int = electric
        self.open_diesel_slot: int = diesel
        self.open_petrol_slot: int = petrol
        self.open_electric_slot: int = electric
        
    def fuel_vehicle(self, fuel_type: str) -> bool:
        time = 1
        if fuel_type == "diesel":
            if self.diesel >= time:
                self.diesel -= 1
                return True
            return False
        elif fuel_type == "petrol":
            if self.petrol >= time:
                self.petrol -= 1
                return True
            return False
        elif fuel_type == "electric":
            if self.electric >= time:
                self.electric -= 1
                return True
            return False
    
    def open_fuel_slot(self, fuel_type: str) -> bool:
        print(self.diesel, self.petrol, self.electric)
        if fuel_type == "diesel":
            if self.diesel < self.open_diesel_slot:
                self.diesel += 1
                return True
            return False
        elif fuel_type == "petrol":
            if self.petrol < self.open_petrol_slot:
                self.petrol += 1
                return True
            return False
        elif fuel_type == "electric":
            if self.electric < self.open_electric_slot:
                self.electric += 1
                return True
            return False
