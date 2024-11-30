
from PIL import ImageGrab
import numpy as np

bbox = (0,104,0+500, 104+280)

image = ImageGrab.grab(bbox=bbox)
image = image.convert("RGB")
image.save("output.png")

array = np.array(image)

