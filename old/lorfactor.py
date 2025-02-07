import math

def calculate_lorentz_factor(v, c=3e8):
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

# Example usage
try:
    velocity = float(input("Enter the velocity of the object (in m/s): "))
    gamma = calculate_lorentz_factor(velocity)
    print(f"The Lorentz factor (γ) for v = {velocity} m/s is: {gamma:.6f}")
except ValueError as e:
    print(e)