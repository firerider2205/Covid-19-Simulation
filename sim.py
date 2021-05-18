#Covid 19 Simulation
import random
import time
import colorama
from colorama import Fore, Back
import sys, os

r0 = 1.27
rate = 4 #days

# current_infected = 22662575 #16.5%
# current_deaths = 246146 #1.1%
# recovered	= 18671222 #82.4%

all_infected = False

CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'

def rewrite(n=1):
    for _ in range(n):
        sys.stdout.write(CURSOR_UP_ONE)
        sys.stdout.write(ERASE_LINE)
 
class Person:
	def __init__(self, infected, population):
		self.died = False
		self.reinfection = False
		self.days = 0
		self.starting_r0 = 2
		self.r0 = 1.27
		self.cont_r0 = 1.1

		self.population = population
		self.infected = infected
		self.all_infected = False
		self.recovered = 0
		self.deaths = 0

	def infectioning(self):
		if self.infected <= self.population:
			if self.infected <= self.population//10:
				self.infected *= self.starting_r0
			elif self.infected > self.population//5:
				self.infected *= self.r0
			elif self.infected > self.population//3:
				self.infected *= self.cont_r0
		elif self.infected >= self.population:
			self.infected = self.population
		
	def recovering(self):
		num1 = random.random()
		num2 = random.randint(0,100)
		num	= num1+num2
		if self.infected >= 30:
			if num <= 60:
				if self.population > self.recovered:
					self.recovered += 1
					self.infected -= 1
		elif self.infected > 100 and self.infected < 1000:
			if num <= 82.4:
				if self.population > self.recovered:
					self.recovered += 1
					self.infected -= 1
		elif self.infected > 1000:
			if num <= 92:
				if self.population > self.recovered:
					self.recovered += 1
					self.infected -= 1

	def dying(self):
		num1 = random.random()
		num2 = random.randint(0,100)
		num	= num1+num2
		if num <= 1.1:
			self.deaths += 1
			self.population -= 1
			self.infected -= 1

	def conditions(self):
		if self.infected + self.recovered + self.deaths != self.population:
			self.days += 1
			if self.days%4 == 0:
				self.infectioning()
			if self.days > 20 and self.days%2 == 0:
				self.recovering()
			if self.days > 100:
				for i in range(4):
					self.recovering()
			if self.days > 1:
				self.dying()
			if self.days > 30:
				for i in range(4):
					self.dying()

person = Person(1, 1000)

while True:
	person.conditions()
	if person.infected	>=  person.population:
		person.all_infected = True

	os.system('clear')
	print()
	print(Fore.GREEN+'Recovered: '+repr(person.recovered))
	print(Fore.WHITE+'')
	rewrite()
	print(Fore.YELLOW+'Population: '+repr(person.population))
	print(Fore.WHITE+'')
	rewrite()
	print(Fore.RED+'Deaths: '+repr(person.deaths))
	print(Fore.WHITE+'')
	rewrite()
	print('Infected: {}'.format(int(person.infected)))
	print(Fore.BLUE+'Days: '+repr(person.days))
	time.sleep(0.05)
	print(Fore.WHITE+'')
	os.system('clear')
	print()
