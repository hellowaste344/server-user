import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
maze = np.array([
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,1],
    [1,1,1,1,1,0,1,0,1,1,1,0,1,0,1,1,1,1,0,1],
    [1,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,1],
    [1,0,1,0,1,1,1,0,1,0,1,1,1,0,1,0,1,1,0,1],
    [1,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,1],
    [1,0,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,1,1,0,0,1],
    [1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,1],
    [1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,0,1],
    [1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,1],
    [1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,1,0,0,1],
    [1,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1],
    [1,0,1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1],
    [1,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
    [1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,0,1,1,1],
    [1,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1],
    [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0]
])

start = (0, 0)
goal = (19, 19)

#number of times the agent will attempt to navigate the maze
num_episodes = 1000
#learning rate that controls how much new information overwrite old information
alpha = None
#discount factor giving more weight to immediate rewards
gamma = 0.4
#probability of exploration vs exploitation; starts higher to explore more
epsilon = 0.8

reward_fire = -10
reward_goal = 50
reward_step = -3

actions = [(0,-1), (0,1), (-1,0), (1,0)]

Q = np.zeros(maze.shape + (len(actions),))

# is_valid ensures the agent can only move inside the maze and avoids obstacles
def is_valid(pos):
    r, c = pos
    if r < 0 or r >= maze.shape[0]:
        return False
    if c < 0 or c >= maze.shape[1]:
        return False
    if maze[r,c] == 1:
        return False
    return True

# choose_action implements exploration vs exploitation strategy
def choose_action(state):
    # np.random.random() generates a random number Range:[0.0, 1.0)
    if np.random.random() < epsilon:
        return np.random.choice(len(actions)) # explore
    else: 
        
        return np.argmax(Q[state])
    
# in order to prevent α decay problem
visit_count = np.zeros_like(Q, dtype=np.int32)
rewards_all_episodes = []

# update Q-Table
for episode in range(num_episodes):
    state = start
    total_rewards = 0
    done = False
    visited_episode = set()

    while not done:
        action_index = choose_action(state)
        action = actions[action_index]

        next_state = (state[0] + action[0], state[1] + action[1])

        visit_count[state][action_index] += 1
        alpha = 1 / (1 + visit_count[state][action_index])

        if not is_valid(next_state):
            reward = reward_fire
            done = True
            next_max = 0
        elif next_state == goal:
            reward = reward_goal
            done = True
            next_max = 0
        else:
            reward = reward_step
            #Penalize LOOPS
            if next_state in visited_episode:
                reward -= 2
            next_max = np.max(Q[next_state])

        visited_episode.add(state)

        old_value = Q[state][action_index]

        # Bellman equation
        Q[state][action_index] = old_value + alpha * (reward + gamma * next_max - old_value)
        if not done:
            state = next_state

        total_rewards += reward
    
        
    # gradually reduce exploration
    epsilon = max(0.01, epsilon * 0.995)

    rewards_all_episodes.append(total_rewards)

# extracting the optimal path after training
def get_optimal_path(Q, start, goal, actions, maze, max_steps=200):
    path = [start]
    state = start
    visited = set()

    for _ in range(max_steps):
        if state == goal:
            break
        visited.add(state)

        best_action = None
        best_value = -float('inf')

        for idx, move in enumerate(actions):
            next_state = (state[0] + move[0], state[1] + move[1])
            
            if(0 <= next_state[0] < maze.shape[0] and 
               0 <= next_state[1] < maze.shape[1] and
               maze[next_state] == 0 and next_state not in visited):
                
                if Q[state][idx] > best_value:
                    best_value = Q[state][idx]
                    best_action = idx
        
        if best_action is None:
            break

        move = actions[best_action]
        state = (state[0] + move[0], state[1] + move[1])
        path.append(state)

    return path

optimal_path = get_optimal_path(Q, start, goal, actions, maze, num_episodes)

# visualization
def plot_maze_with_path(path):
    cmap = ListedColormap(['#eef8ea', "#0D035786"])

    plt.figure(figsize=(8,8))
    plt.imshow(maze, cmap=cmap)

    plt.scatter(start[1], start[0], marker='o', color="#834397", edgecolors='black',
                s=200, label='Start (Robot)', zorder=5)
    plt.scatter(goal[1], goal[0], marker='*', color="#0018ec", edgecolors='black',
                s=300, label='Goal (Diamond)', zorder=5)
    rows, cols = zip(*path)
    plt.plot(cols, rows, color="#d26105", linewidth=4,
             label='Learned Path', zorder=4)

    plt.title("Reinforcement Learning: Robot Maze Navigation")
    plt.gca().invert_yaxis()
    plt.xticks(range(maze.shape[1]))
    plt.yticks(range(maze.shape[0]))
    plt.grid(True, alpha=0.2)
    plt.legend()
    plt.tight_layout()
    plt.show()

plot_maze_with_path(optimal_path)

def plot_rewards(rewards):
    plt.figure(figsize=(10,5))
    plt.plot(rewards)
    plt.title("Learning Curve")
    plt.gca().invert_yaxis()
    plt.xlabel("Episode")
    plt.ylabel("Total Reward")
    plt.grid(True)
    plt.show()

plot_rewards(rewards_all_episodes)