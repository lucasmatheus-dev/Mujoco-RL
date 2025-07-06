import numpy as np

class RandomAgent:
    def __init__(self, action_space):
        self.action_space = action_space

    def act(self, observation):
        #aqui é onde entrará a lógica de ação nova
        return self.action_space.sample()