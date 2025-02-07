'''
Python Program to Calculate the Lorentz Factor
γ is Gama
Relativity: In special relativity, γ (gamma) represents the Lorentz factor
which describes how time, length, and relativistic mass change for an object moving close to the speed of light.
'''

import math

def calculate_lorentz_factor(v, c=3e8):
    """
    Calculate the Lorentz factor (γ) for a given velocity.

    Parameters:
        v (float): Velocity of the object in meters per second (k/s).
        c (float): Speed of light in meters per second (m/s). Default is 3e8 m/s.

    Returns:
        float: Lorentz factor (γ).
    """
    if v >= c:
        raise ValueError("Velocity (v) must be less than the speed of light (c).")
    
    lorentz_factor = 1 / math.sqrt(1 - (v ** 2 / c ** 2))
    return lorentz_factor

# Example usage
try:
    # Input velocity in km/s
    velocity_km_s = float(input("Enter the velocity of the object (in km/s): "))
    
    # Convert km/s to m/s
    velocity_m_s = velocity_km_s * 1e3
    
    # Calculate the Lorentz factor
    gamma = calculate_lorentz_factor(velocity_m_s)
    
    # Output the Lorentz factor
    print(f"\nThe Lorentz factor (γ) for v = {velocity_km_s} km/s is: {gamma:.6f}")
    
    # Explanation of the example
    print("\nExplanation of the Example:")
    print(f"If an object is moving at {velocity_km_s} km/s ({velocity_m_s / 3e8 * 100:.1f}% the speed of light),")
    print(f"the Lorentz factor is approximately {gamma:.3f}. This means:")
    
    # Time dilation
    time_dilation = 1 / gamma
    print(f"\n- Time dilation: For every 1 second that passes for a stationary observer,")
    print(f"  only {time_dilation:.3f} seconds pass for the moving object.")
    
    # Length contraction
    length_contraction = 1 / gamma
    print(f"\n- Length contraction: The object’s length in the direction of motion")
    print(f"  is reduced to {length_contraction:.3f} ({length_contraction * 100:.1f}%) of its rest length.")

except ValueError as e:
    print(e)