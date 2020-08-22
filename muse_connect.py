import sys
import os

from muselsl import stream, list_muses, view, record #For eeg recordings with muse
import subprocess

from time import time, strftime, gmtime
from collections import OrderedDict
import warnings
warnings.filterwarnings('ignore')
#from stroop_stimuli_function import filename, expInfo

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
