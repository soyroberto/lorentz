import math
import numpy as np
import matplotlib.pyplot as plt

'''
γ
The Lorentz factor is the factor by which 
time,
length,
and mass change for an object moving at speeds close to the speed of light (relativistic speeds)
This script calculates the Lorentz factor (γ) for a given velocity and creates a graph of time dilation vs. velocity.
The closes the velocity is to the speed of light:
The more time dilation occurs. ex:  299,792 k/s = 1 year for a stationary observer only 0.64 days pass for the moving object.
'''

def calculate_lorentz_factor(v, c=299_792_458):
    """
    Calculate the Lorentz factor (γ) for a given velocity.

    Parameters:
        v (float): Velocity of the object in meters per second (m/s).
        c (float): Speed of light in meters per second (m/s). Default is 3e8 m/s.

    Returns:
        float: Lorentz factor (γ).
    """
    if v >= c:
        raise ValueError("Velocity (v) must be less than the speed of light (c).")
    
    lorentz_factor = 1 / math.sqrt(1 - (v ** 2 / c ** 2))
    return lorentz_factor

# User Input for Specific Calculation
try:
    velocity_km_s = float(input("Enter the velocity of the object (in km/s): "))
    velocity_m_s = velocity_km_s * 1e3

    # Calculate the Lorentz factor
    gamma = calculate_lorentz_factor(velocity_m_s)
    time_dilation = 1 / gamma

    print(f"\nThe Lorentz factor (γ) for v = {velocity_km_s} km/s is: {gamma:.6f}")
    time_dilation_minutes = 1 * time_dilation  # For 1 minute in the stationary frame
    time_dilation_hours = 1 * time_dilation   # For 1 hour in the stationary frame
    time_dilation_days = 1 * time_dilation    # For 1 day in the stationary frame
    time_dilation_years = 365.25 * time_dilation   # For 1 year in the stationary frame

    print(f"\n  Equivalently:")
    print(f"  - For every 1 minute for the stationary observer, {time_dilation_minutes:.6f} minutes pass for the moving object.")
    print(f"  - For every 1 hour for the stationary observer, {time_dilation_hours:.6f} hours pass for the moving object.")
    print(f"  - For every 1 day for the stationary observer, {time_dilation_days:.6f} days pass for the moving object.")
    print(f"  - For every 1 year for the stationary observer, {time_dilation_years:.6f} days pass for the moving object.")
    print(f"For every 1 year for a stationary observer, {365.25 * time_dilation:.2f} days pass for the moving object.\n")

    # -----------------------------
    # GRAPHING TIME DILATION
    # -----------------------------

    # Generate velocities from 0 to 99.9% of the speed of light
    velocities = np.linspace(0, 0.999 * 3e8, 1000)  # Avoid exactly c to prevent division by zero
    lorentz_factors = 1 / np.sqrt(1 - (velocities ** 2 / (3e8) ** 2))
    time_dilation_factors = 1 / lorentz_factors

    # Plotting Time Dilation vs. Velocity
    plt.figure(figsize=(10, 6))
    plt.plot(velocities / 1e3, time_dilation_factors, label='Time Dilation', color='red')
    
    # Mark the user input on the graph
    plt.scatter([velocity_km_s], [time_dilation], color='blue', s=100, label=f'Your Speed: {velocity_km_s} km/s')
    
    plt.title('Time Dilation vs. Velocity')
    plt.xlabel('Velocity (km/s)')
    plt.ylabel('Fraction of Time Experienced')
    plt.legend()
    plt.grid(True)
    plt.show()

except ValueError as e:
    print(e)
