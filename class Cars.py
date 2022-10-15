class Cars:
	def __init__(self, make, model, year, color, owner):
		self.make = make
		self.model = model
		self.year = year
		self.color = color
		self.owner = owner
    def getDesc(self):
		description =	f'Car Make:		:{self.make}\n'\
						f'Car Model:	:{self.model}\n'\
						f'Car Year:		:{self.year}\n'\
						f'Car Color:	:{self.color}\n'\
						f'Car Owner:	:{self.owner}'
		return description
		
