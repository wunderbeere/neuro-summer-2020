#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.2),
    on Thu Jul 30 16:50:08 2020
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019)
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195.
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard
from multiprocessing import Process

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Setup the Window
win = visual.Window(
    size=(900, 500), fullscr=True, screen=0,
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='height')

# store frame rate of monitor if we can measure it
frameRate = win.getActualFrameRate()
if frameRate != None:
    frameDur = 1.0 / round(frameRate)
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

def baseline_instructions():
    # Initialize components for Routine "instructions"
    instructionsClock = core.Clock()
    instr_cross = visual.TextStim(win=win, name='instr_cross',
        text='You will observe a cross for the next two minutes so that we obtain your resting state brain waves.\n\nThis will give us something to compare your Stroop test brain waves to.\n\nRelax as much as you can (jaw, facial muscles, etc.)\n\n*Press any key to continue.*',
        font='Arial',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0,
        color='white', colorSpace='rgb', opacity=1,
        languageStyle='LTR',
        depth=0.0);
    show_cross = keyboard.Keyboard()

    # ------Prepare to start Routine "instructions"-------
    continueRoutine = True
    # update component parameters for each repeat
    show_cross.keys = []
    show_cross.rt = []
    _show_cross_allKeys = []
    # keep track of which components have finished
    instructionsComponents = [instr_cross, show_cross]
    for thisComponent in instructionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "instructions"-------
    while continueRoutine:
        # get current time
        t = instructionsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instructionsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *instr_cross* updates
        if instr_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instr_cross.frameNStart = frameN  # exact frame index
            instr_cross.tStart = t  # local t and not account for scr refresh
            instr_cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_cross, 'tStartRefresh')  # time at next scr refresh
            instr_cross.setAutoDraw(True)

        # *show_cross* updates
        waitOnFlip = False
        if show_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            show_cross.frameNStart = frameN  # exact frame index
            show_cross.tStart = t  # local t and not account for scr refresh
            show_cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(show_cross, 'tStartRefresh')  # time at next scr refresh
            show_cross.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(show_cross.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(show_cross.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if show_cross.status == STARTED and not waitOnFlip:
            theseKeys = show_cross.getKeys(keyList=None, waitRelease=False)
            _show_cross_allKeys.extend(theseKeys)
            if len(_show_cross_allKeys):
                show_cross.keys = _show_cross_allKeys[-1].name  # just the last key pressed
                show_cross.rt = _show_cross_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "instructions"-------
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

#Funtion that shows the fixation cross
def baseline():
    # Initialize components for Routine "fixation_cross"
    fixation_crossClock = core.Clock()
    cross = visual.TextStim(win=win, name='cross',
        text='+',
        font='Arial',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0,
        color='white', colorSpace='rgb', opacity=1,
        languageStyle='LTR',
        depth=0.0);

    # ------Prepare to start Routine "fixation_cross"-------
    continueRoutine = True
    routineTimer.add(125.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixation_crossComponents = [cross]
    for thisComponent in fixation_crossComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fixation_crossClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "fixation_cross"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixation_crossClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fixation_crossClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *cross* updates
        if cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cross.frameNStart = frameN  # exact frame index
            cross.tStart = t  # local t and not account for scr refresh
            cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cross, 'tStartRefresh')  # time at next scr refresh
            cross.setAutoDraw(True)
        if cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cross.tStartRefresh + 120-frameTolerance:
                # keep track of stop time/frame for later
                cross.tStop = t  # not accounting for scr refresh
                cross.frameNStop = frameN  # exact frame index
                win.timeOnFlip(cross, 'tStopRefresh')  # time at next scr refresh
                cross.setAutoDraw(False)

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixation_crossComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "fixation_cross"-------
    for thisComponent in fixation_crossComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)

    # Flip one final time so any remaining win.callOnFlip()
    # and win.timeOnFlip() tasks get executed before quitting
    win.flip()
    logging.flush()
    # make sure everything is closed down
    win.close()
    core.quit()

if __name__=="__main__":
    import muse_connect
    from stroop_stimuli_function import filename
    baseline_instructions()
    record_baseline_process = Process(target=muse_connect.record_baseline, args=(120, filename + "_baseline.csv"))
    record_baseline_process.start()
    baseline()
