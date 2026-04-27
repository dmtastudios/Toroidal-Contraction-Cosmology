import matplotlib.pyplot as plt
import numpy as np

# Use vector-friendly settings
plt.rcParams.update({
    "font.family": "serif",
    "font.size": 14,
    "axes.linewidth": 1.2,
})

def draw_affine_gauge_schematic():
    fig, ax = plt.subplots(figsize=(8, 6))

    # Base manifold line
    ax.plot([0, 10], [0, 0], color='black', linewidth=2)
    ax.text(5, -0.6, r"Base Manifold $M$", ha='center')

    # Fiber positions
    x_positions = [2, 5, 8]
    for x in x_positions:
        ax.plot([x, x], [0, 3], color='gray', linestyle='--', linewidth=1)
        ax.text(x, 3.2, r"Fiber $G$", ha='center')

    # Horizontal lifts for R and C
    for x in x_positions:
        # C-connection lift (baseline)
        ax.arrow(x, 1.5, 1.5, 0.2, 
                 head_width=0.12, head_length=0.25,
                 length_includes_head=True, color='blue')
        ax.text(x + 1.7, 1.7, r"$C_\mu$", color='blue')

        # R-connection lift (slightly tilted)
        ax.arrow(x, 1.5, 1.5, -0.2, 
                 head_width=0.12, head_length=0.25,
                 length_includes_head=True, color='red')
        ax.text(x + 1.7, 1.3, r"$R_\mu$", color='red')

        # Delta arrow (difference)
        ax.arrow(x + 1.5, 1.5, 0, -0.4,
                 head_width=0.1, head_length=0.15,
                 length_includes_head=True, color='purple')
        ax.text(x + 1.6, 1.0, r"$\Delta_\mu$", color='purple')

    # Curvature loop on the base manifold
    loop_x = [6.5, 7.5, 7.5, 6.5, 6.5]
    loop_y = [0.2, 0.2, -0.2, -0.2, 0.2]
    ax.plot(loop_x, loop_y, color='black')

    # Curvature arrow in fiber
    ax.arrow(7.0, 1.0, 0.0, 0.8,
             head_width=0.12, head_length=0.2,
             length_includes_head=True, color='green')
    ax.text(7.0, 1.9, r"$\mathcal{D}_{\mu\nu}$", color='green', ha='center')

    # Cleanup
    ax.set_xlim(0, 10)
    ax.set_ylim(-1, 4)
    ax.axis('off')

    # Save vector formats
    fig.savefig("Affine_Gauge_Schematic.svg", format="svg")
    fig.savefig("Affine_Gauge_Schematic.pdf", format="pdf")

    plt.show()

draw_affine_gauge_schematic()