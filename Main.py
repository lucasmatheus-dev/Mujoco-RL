import gymnasium as gym
from agents.agent import RandomAgent
import time

def main():
    env = gym.make("Ant-v4", render_mode="human", width=1280, height=720)

    agent = RandomAgent(env.action_space)

    episodes = 5
    steps = 0 

    for i in range(episodes):

        obs, info = env.reset()
        done = False
        total_reward = 0

        while steps <= 10000:
            action = agent.act(obs)
            obs, reward, terminated, truncated, info = env.step(action)
            steps += 1
            done = terminated or truncated

            total_reward += reward

            print("\n" + "="*50)
            print(f" Step: {steps:<5} | Reward: {reward:.4f}")
            print("="*50 + "\n")

            time.sleep(0.03)

    print("\n" + "="*50)
    print("Episódio finalizado. Recompensa total:", total_reward)
    print("="*50 + "\n")
    env.close()

if __name__ == "__main__":
    main()