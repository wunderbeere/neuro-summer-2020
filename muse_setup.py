import sys  # to get file system encoding
from psychopy.hardware import keyboard
from multiprocessing import Process, set_start_method, freeze_support

import sys
import os

from muselsl import stream, list_muses, view, record #For eeg recordings with muse
import subprocess

from time import time, strftime, gmtime
from collections import OrderedDict
import warnings
warnings.filterwarnings('ignore')

#Setup an EEG stream by connecting the muse
def connect_muse ():
    print("\n" + r"If using Windows, install Bluemuse from https://github.com/kowalej/BlueMuse")
    muses = list_muses() #on Windows, you need to use Bluemuse
    if sys.platform.startswith("darwin") or sys.platform.startswith("linux"): #on linux and mac, use muselsl to start the stream
        stream_process = Process(target=stream, args=(muses[0]['address'],))
        stream_process.start()

#Check that muse is streaming
def confirm_streaming ():
    while True:
        confirm = input('Is the muse connected and streaming? [y/n]')
        if confirm == "y":
            break
        else:
            print("\n" + "We'll try to connect again. Please wait.")
            connect_muse()
            continue

#Check signal quality
def check_signal_quality():
    print("\n" + "Starting the visualizer...")
    print("If you want to have a visualizer running in the background, open a new terminal window and type:  muselsl view (or muselsl view -v 2)")
    print("Make sure signal is stable for 20 seconds before continuing \n")
    subprocess.call(['muselsl', 'view', "-v 2"], shell=True)
    while True:
        confirm = input('Is the signal quality acceptable? [y/n]')
        print("\n")
        if confirm == "y":
            break
        else:
            confirm_streaming()
            print("\n" + "Restarting the visualizer...")
            subprocess.call(['muselsl', 'view', "-v 2"], shell=True)
            continue

#record a baseline
def record_baseline(duration, filename):
    print("We will now record a short baseline")
    record(duration, filename, dejitter=True, data_source="EEG")
    print("\n")

#All preliminary muse stuff
if __name__ == "__main__": #this part of the code runs only if you run stroop_main.py in the terminal, not if you import it to another script
    hasMuse = input("Do you have a Muse 2016 that you can connect to the computer? [y/n]")
    if hasMuse == "y":
        connect_muse() #Opening a stream from the muse
        confirm_streaming() #Confirm that the muse is streaming. If it's not, retry to connect.
        check_signal_quality() #Start a visualizer and check signal variance (just a visual exam, for now)

        from stroop_stimuli_function import filename #need this to store the eeg files in the same place as the behavioral experiment data
        from fixationcross_function import baseline, baseline_instructions #import the functions that will show fixation cross and instructions
        baseline_instructions()
        record_baseline_process = Process(target=record_baseline, args=(120, filename + "_baseline.csv"))
        print(record_baseline_process.pid)
        record_baseline_process.start()
        baseline() #show the fixation cross

    elif hasMuse == "n":
        print("\nIf you have a Muse, connect it and calibrate it to your phone now.")
        wantBaseline = input("Would you like to record a 2-minute EEG baseline? [y/n]")
        print("Note that you will need to start the recording manually with your phone.")
        if wantBaseline == "y": #TODO: add other option
            time.sleep(2)
            from fixationcross_function import baseline, baseline_instructions #import the functions that will show fixation cross and instructions
            baseline_instructions()
            baseline()
