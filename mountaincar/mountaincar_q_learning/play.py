import numpy as np
import gym



def idx_to_state(env, state):
    env_low = env.observation_space.low
    env_high = env.observation_space.high
    env_distance = (env_high - env_low) / 50
    position_idx = int((state[0] - env_low[0]) / env_distance[0])
    velocity_idx = int((state[1] - env_low[1]) / env_distance[1])
    state_idx = position_idx + velocity_idx * 50
    return state_idx

if __name__ == '__main__':
    env = gym.make('MountainCar-v0')
    q_table = np.load(file="best_q_table.npy")
    state = env.reset()
    score = 0

    while True:
        env.render()
        state_idx = idx_to_state(env, state)
        action = np.argmax(q_table[state_idx])
        next_state, reward, done, _ = env.step(action)
        print(action)
        next_state_idx = idx_to_state(env, next_state)

        score += reward
        state = next_state

        if done:
            print("Score is %d" % (score))
            break