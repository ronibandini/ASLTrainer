# American Sign Language letter trainer for Texas Instruments AM62A
# Edge Impulse BYOM feature
# Roni Bandini @RoniBandini
# November 2023 MIT License
# https://bandini.medium.com

import subprocess
import time
import json
import random

# Letters in trained model
myLetters= ["A","B","C","D","F","G","J","K","L","O"]

# choose one
selectedLetter=random.choice(myLetters)

# Edge Impulse runner sent to a file for parsing
output_file = open('output.txt', 'w')

# Detection limit
confidenceLimit=0.6

print("American Sign Language Letter Trainer")
print("Texas Instruments AM62A and Edge Impulse BYOM")
print("Roni Bandini, October 2023, Argentina, @RoniBandini")
print("")
print("Stop with CTRL-C")
print("")
print("Please be ready to make the sign for: "+selectedLetter)

# start timers
start = time.time()

# Launch Impulse Runner in a subprocess sending the output to a file
proc1 = subprocess.Popen(["edge-impulse-linux-runner", "--force-engine tidl", "-force-target", "runner-linux-aarch64-am62a"], stdout=output_file)

with open("output.txt", "r") as f:
    lines_seen = set()
    while True:

        line = f.readline()

        if not line:
            time.sleep(1)
            continue

        if ("Want to see a feed" in line):

            print("You can start now")


        if (": '" in line):

            if (selectedLetter in line) and line not in lines_seen:

                # separate using...
                parts = line.split(': ')

                # get second part but last 3 chars
                myConfidence = parts[1][1:-3]
                myConfidence = myConfidence.replace("'", "")
                myConfidence = float(myConfidence)

                # mark as seen
                lines_seen.add(line)

                if myConfidence>confidenceLimit:

                    # calculate ending time

                    end = time.time()

                    print("Well done! I have detected "+selectedLetter+ " with "+str( int(myConfidence*100) )+"% confidence")
                    print("Elapsed time: "+str(int(end - start))+" seconds")

                    #proc1.kill()
                    exit()
                else:
                    print(selectedLetter+ " confidence: " +str( int(myConfidence*100) )+"%")
