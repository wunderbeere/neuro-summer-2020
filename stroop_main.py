from muselsl import record
from stroop_stimuli_function import stroop_stimuli, filename
from multiprocessing import Process, freeze_support


input("Press any key when you are ready to start the Stroop experiment with Muse (More instructions will follow).\n")

if __name__ == '__main__':
    #freeze_support()
    #stroop_stimuli_process = Process(target=stroop_stimuli)
    recording_process = Process(target=record, args=(300, filename + "_eeg.csv"))
    
#this works but is really really buggy

    #stroop_stimuli_process.start()
    recording_process.start()
    stroop_stimuli()
    #stroop_stimuli_process.join()
    #recording_process.join()
