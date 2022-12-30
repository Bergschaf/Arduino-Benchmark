import os
import subprocess
import time

ARDUINO_CLI = "./arduino-cli.exe"
SKETCHES = os.listdir("sketches")
times = []


def get_boards():
    boards = [p.split(" ") for p in
              subprocess.run(["arduino-cli", "board", "list"],
                             capture_output=True).stdout.decode(
                  "utf-8").split("\n")[1:] if "arduino" in p]
    if len(boards) == 0:
        print("No boards found, connect a board and try again")
        exit()
    print("Boards found:")
    for i, b in enumerate(boards):
        print(f"{i + 1}. {b[0]} - {b[-2]}")
    return [(b[0], b[-2]) for b in boards]

if __name__ == '__main__':
    port = get_boards()[0][0]
    for sketch in SKETCHES:
        start = time.time()
        subprocess.run([ARDUINO_CLI, "upload", "--fqbn", "arduino:avr:uno","sketches/" + sketch, "-p", port])
        times.append((sketch,(time.time() - start).__round__(3)))
    print(times)