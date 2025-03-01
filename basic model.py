import matplotlib.pyplot as plt
import math
import numpy as np
plt.rcParams.update({'font.size': 20})
m_rocket = 10000
v_e = 3000
g = 9.81
a = 0.38 * g
u = 11200
mars = 54600000000
v_halfway_mars = math.sqrt(u**2 + a*mars)
asteroid_belt = 175000000000
n = 1000
distances = np.linspace(0, asteroid_belt, n)

velocities = []
for s in distances:
  v = math.sqrt(u**2 + a*s) #dont multiply by 2 because halving anyway
  velocities.append(v)

delta_Vs = []
for v in velocities:
  delta_V = 2 * (v - u)
  delta_Vs.append(delta_V)

fuels = []
for delta_V in delta_Vs:
  fuel = m_rocket * (math.e**(delta_V/v_e) - 1)
  fuels.append(fuel)

def plot_objects(name, s, colour):
    v = math.sqrt(11200 ** 2 + 0.38 * s * 9.81)
    delta_V = 2 * (v-u)
    fuel = m_rocket * (math.e**(delta_V/v_e) - 1)
    print(name, ": ", fuel)
    plt.plot(s, fuel, colour, label=name)

plt.plot(distances, fuels)

plot_objects("Mars", 54600000000, "ro") #mars
plot_objects("Moon", 360000000, "ko") #moon
plot_objects("Asteroid belt", 175000000000, "mo") #asteroid belt

plt.xscale("log")
plt.yscale("log")

plt.legend(loc="lower right")
plt.ylabel("Mass (kg)")
plt.xlabel("Distance from Earth (m)")
plt.title("Effect of distance travelled on mass of fuel required")
plt.show()
