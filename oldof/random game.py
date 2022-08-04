import os
import random
import subprocess
dir = "C:/Games/Random game/"

file = os.path.join(dir, random.choice(os.listdir(dir)));
file = random.choice(os.listdir(dir))

subprocess.Popen(file)