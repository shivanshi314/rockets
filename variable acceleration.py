def solve_quadratic(a, b, c):
    d = (b ** 2) - (4 * a * c)
    sol1 = (-b - math.sqrt(d)) / (2 * a)
    sol2 = (-b + math.sqrt(d)) / (2 * a)
    if sol1>0:
        return sol1
    else:
        return sol2

def linear_model(frac):
    #constant deceleration
    g_metres = 9.81
    distance_mars = 54600000000

    #linear bit
    T_c =  solve_quadratic(0.27 * g_metres, 11200, -1 * frac * distance_mars) #(u_Tc - 11200)/(0.35 * g_metres)
    T_0 = T_c/1.38

    def v(t):
        return (-0.69 * g_metres/T_c)*t**2 + g_metres*t + 11200

    ve = g_metres * 600

    dv1 = abs(v(T_0) - 11200)
    dv2 = abs(v(T_c) - v(T_0))
    dv3 = abs(v(T_c) - 11200)
    delta_v = dv1 + dv2 + dv3
    fuel = m_rocket * (math.e ** (delta_v / ve) - 1)

    return(delta_v, fuel)

print(linear_model(0.1))

fractions = []
a=0.0005

b=0.9
for i in range(101):
    fractions.append((b-a)*i/100 + a)

delta_Vs = []
fuelsss = []

for j in range(len(fractions)):
    delta_Vs.append(linear_model(fractions[j])[0])
    fuelsss.append(linear_model(fractions[j])[1])

plt.subplot(1, 2, 1)
plt.plot(fractions, delta_Vs)
plt.title("Delta V")
plt.xlabel("Fraction of journey covered under decreasing acceleration")
plt.ylabel("Delta V")

plt.subplot(1, 2, 2)
plt.plot(fractions, fuelsss)
plt.title("Fuel required")
plt.xlabel("Fraction of journey covered under decreasing acceleration")
plt.ylabel("Fuel (kg)")


plt.suptitle("Effect of changing the starting point of constant acceleration on: ")
plt.show()
