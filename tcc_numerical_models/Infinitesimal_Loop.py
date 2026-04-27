import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    "font.family": "serif",
    "font.size": 14,
    "axes.linewidth": 1.2,
})

def draw_curvature_loop_schematic():
    fig, ax = plt.subplots(figsize=(8, 6))

    # Base manifold rectangle (infinitesimal loop)
    loop_x = [3, 6, 6, 3, 3]
    loop_y = [0, 0, 1.5, 1.5, 0]
    ax.plot(loop_x, loop_y, color='black', linewidth=2)
    ax.text(4.5, -0.4, r"Infinitesimal Loop in $M$", ha='center')

    # Fiber above starting point
    ax.plot([3, 3], [0, 3], color='gray', linestyle='--')
    ax.text(3, 3.2, r"Fiber $G$", ha='center')

    # Fiber above ending point
    ax.plot([6, 6], [0, 3], color='gray', linestyle='--')
    ax.text(6, 3.2, r"Fiber $G$", ha='center')

    # Horizontal lifts along the loop using R-connection
    # Start point
    x0, y0 = 3, 1.5
    ax.text(x0 - 0.2, y0 + 0.2, r"Start", ha='right')

    # Lift along first edge
    ax.arrow(x0, y0, 1.5, 0.15,
             head_width=0.12, head_length=0.25,
             length_includes_head=True, color='red')

    # Lift along second edge
    ax.arrow(4.5, 1.65, 0.15, -1.2,
             head_width=0.12, head_length=0.25,
             length_includes_head=True, color='red')

    # Lift along third edge
    ax.arrow(4.65, 0.45, -1.5, -0.15,
             head_width=0.12, head_length=0.25,
             length_includes_head=True, color='red')

    # Lift along fourth edge
    ax.arrow(3.15, 0.3, -0.15, 1.2,
             head_width=0.12, head_length=0.25,
             length_includes_head=True, color='red')

    # Final point (does not close)
    ax.text(3.0, 1.0, r"End", ha='right')

    # Curvature displacement arrow
    ax.arrow(3.0, 1.0, 0.0, 0.5,
             head_width=0.12, head_length=0.2,
             length_includes_head=True, color='green')
    ax.text(3.1, 1.5, r"$\mathcal{D}_{\mu\nu}$", color='green')

    # Cleanup
    ax.set_xlim(2, 7)
    ax.set_ylim(-1, 4)
    ax.axis('off')

    # Save vector formats
    fig.savefig("Curvature_Loop_Schematic.svg", format="svg")
    fig.savefig("Curvature_Loop_Schematic.pdf", format="pdf")

    plt.show()

draw_curvature_loop_schematic()