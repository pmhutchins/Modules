class Favcar:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def getDesc(self):
        description = (
            f"Car Make:     :{self.make}\n"
            f"Car Model:    :{self.model}\n"
            f"Car Year:     :{self.year}\n"
            f"Car Color:    :{self.color}"
        )
        return description

    netFavcar1 = Favcar("Pontiac", "TransAm", "2002", "Black")
    netFavcar2 = Favcar("Chevrolet", "Silverado", "2001", "Burgundy")
    netFavcar3 = Favcar("Dodge", "Ram", "2022", "Black")
    netFavcar4 = Favcar("Chevrolet", "Impala", "2022", "Black")
    netFavcar5 = Favcar("Chevrolet", "Camaro", "2022", "Black")
