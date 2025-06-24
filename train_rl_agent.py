import numpy as np

# Environment for crossing the road
class RoadCrossingEnv:
    def __init__(self):
        self.positions = 4  # 0 to 3 (start to end)
        self.target_sequence = ['right', 'left', 'right']
        self.reset()

    def reset(self):
        self.position = 0  # Start at position 0
        self.current_step = 0  # Track step in sequence 
        self.state = (self.position, self.current_step)
        return self.state

    def step(self, action):
        action = 'right' if action == 1 else 'left'
        done = False
        reward = -0.1  # Small penalty per step

        # Check if action matches target sequence
        if self.current_step < len(self.target_sequence):
            if action == self.target_sequence[self.current_step]:
                # Correct action
                if action == 'right' and self.position < self.positions - 1:
                    self.position += 1
                elif action == 'left' and self.position > 0:
                    self.position -= 1
                self.current_step += 1  # Increment current_step (RENAMED)

                # Check if sequence is complete
                if self.current_step == len(self.target_sequence):
                    reward = 10.0  # Big reward for completing sequence
                    done = True
            else:
                # Wrong action
                reward = -1.0
        else:
            done = True

        self.state = (self.position, self.current_step)
        return self.state, reward, done

# Q-learning agent
class QLearningAgent:
    def __init__(self, state_space, action_space, lr=0.1, gamma=0.9, epsilon=0.1):
        self.q_table = np.zeros(state_space + (action_space,))
        self.lr = lr
        self.gamma = gamma
        self.epsilon = epsilon
        self.action_space = action_space

    def choose_action(self, state):
        if np.random.random() < self.epsilon:
            return np.random.randint(self.action_space)
        return np.argmax(self.q_table[state])

    def update(self, state, action, reward, next_state):
        best_next_action = np.argmax(self.q_table[next_state])
        td_target = reward + self.gamma * self.q_table[next_state][best_next_action]
        td_error = td_target - self.q_table[state][action]
        self.q_table[state][action] += self.lr * td_error

# Training loop
def train_agent(episodes=1000):
    env = RoadCrossingEnv()
    agent = QLearningAgent(state_space=(env.positions, len(env.target_sequence) + 1), 
                          action_space=2,  # 0: left, 1: right
                          lr=0.1, gamma=0.9, epsilon=0.1)
    
    total_rewards = []
    
    for episode in range(episodes):
        state = env.reset()
        episode_reward = 0
        done = False
        
        while not done:
            action = agent.choose_action(state)
            next_state, reward, done = env.step(action)
            agent.update(state, action, reward, next_state)
            state = next_state
            episode_reward += reward
        
        total_rewards.append(episode_reward)
        
        # Decay epsilon
        agent.epsilon = max(0.01, agent.epsilon * 0.995)
        
        if (episode + 1) % 100 == 0:
            avg_reward = np.mean(total_rewards[-100:])
            print(f"Episode {episode + 1}, Average Reward: {avg_reward:.2f}")
    
    return agent, total_rewards

# Test the trained agent
def test_agent(agent, episodes=5):
    env = RoadCrossingEnv()
    for episode in range(episodes):
        state = env.reset()
        done = False
        actions = []
        
        while not done:
            action = agent.choose_action(state)
            action_name = 'right' if action == 1 else 'left'
            actions.append(action_name)
            state, reward, done = env.step(action)
        
        print(f"Test Episode {episode + 1}, Actions: {actions}, Final Reward: {reward:.2f}")

if __name__ == "__main__":
    # Train the agent
    trained_agent, rewards = train_agent(episodes=1000)
    
    # Test the agent
    print("\nTesting trained agent:")
    test_agent(trained_agent, episodes=5)