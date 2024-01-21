import numpy as np
import matplotlib.pyplot as plt

def brownian_motion(num_steps, step_size=1):
    """Simulate 1D Brownian motion."""
    steps = np.random.normal(0, step_size, num_steps)
    return np.cumsum(steps)

def plot_brownian_motion(num_steps, step_size=1):
    """Generate and plot Brownian motion."""
    path = brownian_motion(num_steps, step_size)

    plt.figure(figsize=(10, 6))
    plt.plot(range(num_steps), path, label='Brownian Motion')
    plt.title('1D Brownian Motion Simulation')
    plt.xlabel('Time Steps')
    plt.ylabel('Position')
    plt.legend()
    plt.grid(True)
    plt.show()

# Set the number of steps and step size
num_steps = 1000
step_size = 0.1

# Generate and plot Brownian motion
plot_brownian_motion(num_steps, step_size)
