from stable_baselines3.common.env_checker import check_env
from snakegame_env import SnakeEnv

env = SnakeEnv()
episodes = 50

for episode in range(episodes):
    done = False
    obs = env.reset()
    while True: 
        random_action = env.action_space.sample()
        print("action",random_action)
        obs, reward, done, info = env.step(random_action)
        print('reward',reward)
# check_env(env)