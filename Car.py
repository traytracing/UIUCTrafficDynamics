import numpy as np
import pyplot as plt
from scipy.integrate import solve_ivp

class Road:
    def __init__(self, stopsigns, cars, n = 2):
        self.roadData = [0] * n
        for i in range(n):
            self.roadData[i] = 0
            
        for i in range(len(stopsigns)):
            self.roadData[i] = 1

        self.cars = cars
        return


class Car:
    
    def __init__(self, x=0, v=0, a=0, tau=0):
        self.x = x # position
        self.v = v # velocity
        self.a = a # acceleration
        self.tau = tau # reaction time

    def step(self, dt):
        sol_x = solve_ivp(v, )
    
    


cars = []

for i in range(10):
    cars.append(Car(i))

stopsigns = []

road = Road(stopsigns, cars, 10)

for car in road.cars:
    plt.scatter(car.x, 0)
plt.show()
