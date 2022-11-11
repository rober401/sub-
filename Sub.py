# library's
import os
import random
import names

import numpy as np
import matplotlib.pyplot as plt

os.system("cls")

# ------------------------------------------------------------------

# Vars
Time_x = random.randint(1,9)
Time_y = random.randint(10,59)
Time = (f"{Time_x}:{Time_y}")

Position = "surfaced"

def status():
    print(f"Time : {Time}")
    print(f"Position : {Position}")
    print("\n\n")


# Radar
def Radar_gen():

    random_dir = random.randint(1,4)
    if random_dir == 1:
        # east
        E = random.randint(25,100)
        N = 0
        W = 0
        S = 0
        print(f"Target approaching from the East\n{E} Miles away")

    elif random_dir == 2:
        # North
        E = 0
        N = random.randint(25,100)
        W = 0
        S = 0
        print(f"Target approaching from the North\n{N} Miles away")

    elif random_dir == 3:
        # West
        E = 0
        N = 0
        W = random.randint(25,100)
        S = 0
        print(f"Target approaching from the West\n{W} Miles away")

    else:
        # South
        E = 0
        N = 0
        W = 0
        S = random.randint(25,100)
        print(f"Target approaching from the South\n{S} Miles away")

    plt.style.use('ggplot')

    subjects = ['East', 'North', 'West', 'South']
    unknown = [E, N, W, S]  # change this one to change Position of unknown target

    You = [0, 0, 0, 0]

    angles = np.linspace(0, 2 * np.pi, len(subjects), endpoint=False)

    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, polar=True)

    # unknown ship
    ax.plot(angles, unknown, 'o-', color='g', linewidth=1, label='unknown')
    ax.fill(angles, unknown, alpha=0.25, color='g')

    # Player sub
    ax.plot(angles, You, 'o-', color='orange', linewidth=1, label='You')
    ax.fill(angles, You, alpha=0.25, color='orange')

    ax.set_thetagrids(angles * 180 / np.pi, subjects)
    plt.grid(True)
    plt.tight_layout()
    plt.legend()
    plt.show()


status()
Radar_gen()
