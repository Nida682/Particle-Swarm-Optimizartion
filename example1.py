import random

# Simulated loss function (like neural network error)
# Goal: minimize error
def loss(weight):
    target_weight = 2.5   # ideal weight (unknown in real case)
    return (weight - target_weight) ** 2

# Initialize particles (weights)
particles = [random.uniform(-5, 5) for _ in range(5)]
velocities = [0] * 5

# Personal best and global best
p_best = particles[:]
g_best = min(particles, key=loss)

for iteration in range(10):
    for i in range(len(particles)):
        # Update velocity
        velocities[i] = (0.5 * velocities[i] +
                         0.8 * (p_best[i] - particles[i]) +
                         0.9 * (g_best - particles[i]))

        # Update position (weight)
        particles[i] += velocities[i]

        # Update personal best
        if loss(particles[i]) < loss(p_best[i]):
            p_best[i] = particles[i]

    # Update global best
    g_best = min(p_best, key=loss)

    print("Iteration:", iteration, "Best Weight:", round(g_best, 4), "Loss:", round(loss(g_best), 4))
