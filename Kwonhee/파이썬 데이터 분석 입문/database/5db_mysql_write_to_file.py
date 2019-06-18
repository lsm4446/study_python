class Car:
	honk = "빵빵"

	def info(self, color, year):
		print "color : %s ,year: %d" % (color, year)

new_car = Car()
new_car.info("Red",2017)
