import matplotlib.pyplot as plt

# Circuit diagram of the 8051 microcontroller-based Smart Railway Gate Controller
plt.figure(figsize=(8, 6))
plt.title("8051 Microcontroller-based Smart Railway Gate Controller")
plt.xlabel("Components")
plt.ylabel("Connections")

# IR Sensor
plt.plot([1, 2], [1, 1], 'bo-')
plt.text(1.5, 1.1, "IR Sensor")

# 8051 Microcontroller
plt.plot([2, 3], [1, 1], 'bo-')
plt.text(2.5, 1.1, "8051 Microcontroller")

# Relay Module
plt.plot([3, 4], [1, 1], 'bo-')
plt.text(3.5, 1.1, "Relay Module")

# Power Supply
plt.plot([4, 5], [1, 1], 'bo-')
plt.text(4.5, 1.1, "Power Supply")

plt.show()
# Circuit diagram of the AVR microcontroller-based Smart Railway Gate Controller
plt.figure(figsize=(8, 6))
plt.title("AVR Microcontroller-based Smart Railway Gate Controller")
plt.xlabel("Components")
plt.ylabel("Connections")

# IR Sensor
plt.plot([1, 2], [1, 1], 'bo-')
plt.text(1.5, 1.1, "IR Sensor")

# AVR Microcontroller
plt.plot([2, 3], [1, 1], 'bo-')
plt.text(2.5, 1.1, "AVR Microcontroller")

# Motor Driver
plt.plot([3, 4], [1, 1], 'bo-')
plt.text(3.5, 1.1, "Motor Driver")

# Power Supply
plt.plot([4, 5], [1, 1], 'bo-')
plt.text(4.5, 1.1, "Power Supply")

plt.show()