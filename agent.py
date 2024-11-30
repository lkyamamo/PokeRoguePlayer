import torch
import random
import numpy as np
import os
import sys
from collections import deque
from PIL import ImageGrab
import numpy as np
import json

MAX_MEMORY = 100_000
BATCH_SIZE = 1000
LR = 0.001
BBOX = (0,104,0+500, 104+280)

class Game:
       def __init__(self, bbox):
              self.bbox = bbox

              with open('species.json', 'r') as file:
                     species = json.load(file)

       #move only defined as left, right, up, down, or select
       def play_step(self, move):
              pass





class Agent:

       def __init__(self):
            self.n_games = 0
            self.epslilon = 0 #randomness
            self.gamma = 0 # discount rate
            self.memory = deque(maxlen=MAX_MEMORY) # popleft()
            # TODO: model, trainer

       def get_state(self):

              BBOX = (0,104,0+500, 104+280)

              image = ImageGrab.grab(bbox=bbox)
              image = image.convert("RGB")
              image.save("output.png")

              array = np.array(image)
        
       def remember(self, state, action, reward, next_state, done):
              pass
        
       def train_long_memory(self):
              pass
        
       def train_short_memory(self,  state, action, reward, next_state, done):
              pass
               
       def get_action(self, state):
              pass
        
       def play_step(self, ):
              pass

def train():
       plot_scores = []
       plot_mean_scores = []
       total_score = 0
       record = 0
       agent = Agent()
       game = Game()

       while True:
              # get old state
              state_old = game.get_state()

              # get move
              final_move = agent.get_action(state_old)

              # perform move and get new state
              reward, done, score = game.play_step(final_move)
              state_new = game.get_state(game)

              # train short memory
              agent.train_short_memory(state_old, final_move, reward, state_new, done)

              # remember
              agent.remember(state_old, final_move, reward, state_new, done)

              if done:
                     # train long mem
                     game.reset()
                     agent.n_games += 1
                     agent.train_long_memory()

                     if score > record:
                            record = score
                            # agent.mode.save()

                     print('Game', agent.n_games, 'Score', score, 'Record:', record)
                     
                     # plot


if __name__ == '__main__':
       train()