import os
import subprocess
import time

ARDUINO_CLI = "./arduino-cli.exe"
SKETCHES = os.listdir("sketches")
times = []
if __name__ == '__main__':
    for sketch in SKETCHES:
        start = time.time()
        subprocess.run([ARDUINO_CLI, "compile", "--fqbn", "arduino:avr:uno","sketches/" + sketch])
        times.append((sketch,(time.time() - start).__round__(3)))
    print(times)