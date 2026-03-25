import random

# Target position (goal location)
target = 50

# Fitness function (distance to target)
def distance(position):
    return abs(target - position)  # minimize distance

# Initialize particles (positions)
particles = [random.uniform(0, 100) for _ in range(5)]
velocities = [0] * 5

# Personal best and global best
p_best = particles[:]
g_best = min(particles, key=distance)

for iteration in range(10):
    for i in range(len(particles)):
        # Update velocity
        velocities[i] = (0.5 * velocities[i] +
                         0.7 * (p_best[i] - particles[i]) +
                         0.9 * (g_best - particles[i]))

        # Update position
        particles[i] += velocities[i]

        # Keep within bounds (0–100)
        particles[i] = max(0, min(100, particles[i]))

        # Update personal best
        if distance(particles[i]) < distance(p_best[i]):
            p_best[i] = particles[i]

    # Update global best
    g_best = min(p_best, key=distance)

    print("Iteration:", iteration, "Best Position:", round(g_best, 2), "Distance:", round(distance(g_best), 2))
