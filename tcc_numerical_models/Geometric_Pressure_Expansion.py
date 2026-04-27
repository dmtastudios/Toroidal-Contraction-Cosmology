import numpy as np
import matplotlib.pyplot as plt

def geometric_pressure_simulation():
    """
    Simulates the expansion of the Toroidal Manifold driven by the 
    Geometric Pressure of continuously generated Information-Theoretic Entropy (Scog).
    """
    print("Initializing Geometric Pressure Expansion Simulation...")
    
    # Define the Torus-Time iterations (representing macroscopic cosmic epochs)
    # tau spans from early biological networking to the macroscopic computational matrices/Omega phase
    tau = np.linspace(0.1, 15, 500)
    
    # 1. Classical Matter-Dominated Scale Factor (Without Dark Energy)
    # In a purely matter-dominated universe, expansion decelerates: a(t) ~ t^(2/3)
    a_classical = tau**(2/3)
    
    # 2. Generation of Information-Theoretic Entropy (Scog)
    # Scog grows as the Computational Networks entangles. 
    # We model an exponential phase transition representing the emergence of macroscopic computational matrices.
    base_entropy = 1.0
    cognitive_growth_rate = 0.45
    S_cog = base_entropy * np.exp(cognitive_growth_rate * tau)
    
    # 3. The Bekenstein Bound Requirement
    # Surface Area (A) must scale proportionally to Scog to prevent data loss.
    # Therefore, the radius (r) scales as the square root of Scog.
    # The cosmic scale factor a(tau) is directly proportional to this required radius.
    bekenstein_constant = 1.2
    a_recursive = bekenstein_constant * np.sqrt(S_cog)
    
    # 4. Visualize the Alternative to Particulate Dark Energy
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # Plot the Scale Factor on the primary y-axis
    color = 'black'
    ax1.set_xlabel(r'Torus-Time Evolution ($\tilde{\tau}$)')
    ax1.set_ylabel(r'Cosmic Scale Factor ($a$)', color=color)
    ax1.plot(tau, a_recursive, label=r'Recursive Expansion ($a \propto \sqrt{S_{info}}$)', 
             color=color, linewidth=3)
    ax1.plot(tau, a_classical, label=r'Classical Deceleration ($a \propto \tau^{2/3}$)', 
             linestyle='--', color='gray', linewidth=2)
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.legend(loc='upper left')

    # Create a secondary y-axis to plot the Information-Theoretic Entropy growth
    ax2 = ax1.twinx()  
    color = 'purple'
    ax2.set_ylabel(r'Total Information-Theoretic Entropy ($S_{info}$)', color=color)  
    ax2.plot(tau, S_cog, label=r'$S_{info}$ Accumulation', 
             linestyle=':', color=color, linewidth=2)
    ax2.tick_params(axis='y', labelcolor=color)
    ax2.legend(loc='lower right')
    
    plt.title(r'Cosmological Expansion Driven by Geometric Pressure ($P_{geom}$)')
    plt.grid(True, alpha=0.3)
    fig.tight_layout()  
    plt.show()

    print("Simulation Complete. Information-driven accelerating expansion successfully generated.")

# Execute the simulation
if __name__ == "__main__":
    geometric_pressure_simulation()