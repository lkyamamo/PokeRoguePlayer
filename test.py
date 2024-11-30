import torch
import random
import numpy as np
import os
import sys
from collections import deque
from PIL import ImageGrab
import numpy as np
import json

# Open the JSON file
def import_species():

    with open('species.json', 'r') as file:
        species = json.load(file)
        return species
    
def take_screenshot():
    bbox = (0,104,0+500, 104+280)

    image = ImageGrab.grab(bbox=bbox)
    image = image.convert("RGB")
    image.save("output.png")

    array = np.array(image)
    return array
