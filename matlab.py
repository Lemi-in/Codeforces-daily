import numpy as np

# Given data
y_R = np.array([0.0030, 0.0034, 0.0041, 0.0051, 0.0055, 0.0061, 0.0075, 0.0075, 0.0082])
u_U = np.array([0.140, 0.152, 0.179, 0.221, 0.228, 0.264, 0.300, 0.318, 0.343])
R = 4.86  # radius
U = 9.8  # velocity
mu = 3.8 * 10**-7  # dynamic viscosity

# Convert the given non-dimensional data back to dimensional form
y = y_R * R
u = u_U * U

# Calculate the derivative du/dy
du_dy = np.gradient(u, y)

# Calculate the shear stress tau
tau = mu * du_dy

# Display the results
print('Shear stress tau:')
print(tau)

# Define the FirstDerivUneq function to calculate tau
def FirstDerivUneq(u, y, mu):
    du_dy = np.gradient(u, y)
    tau = mu * du_dy
    return tau

# Call the function and pass the parameters
tau_calculated = FirstDerivUneq(u, y, mu)
print('Calculated shear stress using function:')
print(tau_calculated)
