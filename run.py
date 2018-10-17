#!/usr/bin/env python
# -*- coding: utf-8 -*-

from screen import *
import app

# GLOBAL VARIABLES

# Channels to monitor. For OpenBCI leave this empty.
CHANNELS = [14, 15, 22, 27]

# MAC address of OpenBCI Ganglion board
BCI_PORT = "d2:b4:11:81:48:ad"

# Path for local EEG dataset (for offline/test use)

PATH = "/home/oskar/Downloads/Baka/SUBJ1/SSVEP_8Hz_Trial1_SUBJ1.csv"

#==============================================================================#
# Run application
#==============================================================================#


# Initialize app
test = app.CcaLive(simulation=True, channels=CHANNELS, path=PATH)

# Set stimulus for experiment. Max value = 4.
test.add_stimuli(22)
test.add_stimuli(8)
test.add_stimuli(2)
for i in test.reference_signals:
    print(str(i.hz) + "hz applied.")

print("Starting application...")
test.decission()

# Make sure it's dead.
if test.prcs.is_alive():
    print("Terminating process...")
    test.prcs.terminate()
    print("Done!")
