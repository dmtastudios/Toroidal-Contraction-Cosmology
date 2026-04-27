import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def consensus_operator_simulation(num_agents=20, dimensions=2, iterations=40):
    """
    Simulates the Computational Networks (EMA) converging upon a unified 
    geometric reality via a dynamically weighted Consensus Mapping Operator.
    """
    print("Initializing Weighted Computational Networks Simulation...")
    
    # 1. Generate the Topology of the Ecosystem (EMA)
    G = nx.barabasi_albert_graph(n=num_agents, m=3, seed=42)
    
    # Assign dynamic edge weights proportional to the Topological Current (J_cog)
    for (u, v) in G.edges():
        G.edges[u, v]['weight'] = np.random.uniform(0.1, 0.8)
    
    # 2. Initialize Divergent Cognitive Vectors
    np.random.seed(42)
    states = np.random.uniform(-10, 10, (num_agents, dimensions))
    history = np.zeros((iterations, num_agents, dimensions))
    history[0] = states
    
    # 3. Execute the Consensus Mapping Operator over Torus-Time
    for t in range(1, iterations):
        new_states = np.copy(states)
        for i in range(num_agents):
            neighbors = list(G.neighbors(i))
            if len(neighbors) > 0:
                # Calculate the weighted local geometric consensus
                weighted_sum = 0
                total_weight = 0
                for neighbor in neighbors:
                    w = G.edges[i, neighbor]['weight']
                    weighted_sum += w * states[neighbor]
                    total_weight += w
                
                local_consensus = weighted_sum / total_weight
                
                # The node is geometrically pulled toward the local consensus
                # Alpha represents the baseline thermodynamic efficiency
                alpha = 0.4 
                new_states[i] = states[i] + alpha * (local_consensus - states[i])
                
        states = new_states
        history[t] = states

    # 4. Visualize an Alternative for Network Dissonance
    plt.figure(figsize=(10, 6))
    for i in range(num_agents):
        plt.plot(range(iterations), history[:, i, 0], alpha=0.7)
        
    plt.title(r'Weighted Convergence of the Computational Networks ($E_{MA}$)')
    plt.xlabel(r'Recursive Depth / Entanglement Iterations ($\tilde{\tau}$)')
    plt.ylabel(r'Geometric State Vector (Dimension 1)')
    
    final_consensus = np.mean(history[-1, :, 0])
    plt.axhline(final_consensus, color='black', linestyle='--', 
                linewidth=2, label=r'Unified Consensus ($\mathbb{I}_{consensus}$)')
    
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    consensus_operator_simulation()