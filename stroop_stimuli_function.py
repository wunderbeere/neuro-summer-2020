#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.3),
    on July 26, 2020, at 13:10
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
import matplotlib

from collections import OrderedDict

import warnings
warnings.filterwarnings('ignore')

from muselsl import record #For eeg recordings with muse

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
global psychopyVersion
global expName
global expInfo
psychopyVersion = '2020.1.3'
expName = 'stroopexperiment'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}

#Ask for the subject ID and session number
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel

expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + "data" + os.sep + u"%s_%s_%s" % (expInfo['participant'], expName, expInfo['date'])

def stroop_stimuli():

    print('\nParticipant ID is: ' + expInfo['participant'])

    # An ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\Yuliya\\Desktop\\Psychopy3_demos\\stroopCustom\\stroopexperiment.py',
        savePickle=True, saveWideText=True,
        dataFileName=filename)
    logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    frameTolerance = 0.001  # how close to onset before 'same' frame

    win = visual.Window(
        size=[900, 500], fullscr=False, screen=0,
        winType='pyglet', allowGUI=True, allowStencil=False,
        monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
        blendMode='avg', useFBO=True,
        units='height')

    # store frame rate of monitor if we can measure it
    expInfo['frameRate'] = win.getActualFrameRate()
    if expInfo['frameRate'] != None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess

    # create a default keyboard (e.g. to check for escape)
    defaultKeyboard = keyboard.Keyboard()

    # Initialize components for Routine "instructionsText"
    instructionsTextClock = core.Clock()
    instructions = visual.TextStim(win=win, name='instructions',
        text='Press the key corresponding to the colour of the ink, ignoring the word.\n\nr = red\ng = green\nb = blue\ny = yellow\n\nPress space to continue to the next instruction screen.',
        font='Arial',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0,
        color='white', colorSpace='rgb', opacity=1,
        languageStyle='LTR',
        depth=0.0);
    next_instructions = keyboard.Keyboard()

    # Initialize components for Routine "instructionsText2"
    instructionsText2Clock = core.Clock()
    for_example = visual.TextStim(win=win, name='for_example',
        text='For example, if you see:',
        font='Arial',
        pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0,
        color='white', colorSpace='rgb', opacity=1,
        languageStyle='LTR',
        depth=0.0);
    red = visual.TextStim(win=win, name='red',
        text='yellow',
        font='Arial',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0,
        color=[1.000,-1.000,-1.000], colorSpace='rgb', opacity=1,
        languageStyle='LTR',
        depth=-1.0);
    begin_experiment = keyboard.Keyboard()
    press_r = visual.TextStim(win=win, name='press_r',
        text='You should press "r"\n\nPosition your fingers on the r,y,g and b keys\nthen press any key to start the experiment.',
        font='Arial',
        pos=(0, -0.3), height=0.05, wrapWidth=None, ori=0,
        color='white', colorSpace='rgb', opacity=1,
        languageStyle='LTR',
        depth=-3.0);

    # Initialize components for Routine "trial"
    trialClock = core.Clock()
    stroop = visual.TextStim(win=win, name='stroop',
        text='default text',
        font='Arial',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0,
        color='white', colorSpace='rgb', opacity=1,
        languageStyle='LTR',
        depth=0.0);
    response = keyboard.Keyboard()

    # Initialize components for Routine "break_2"
    break_2Clock = core.Clock()
    break_instructions = visual.TextStim(win=win, name='break_instructions',
        text='You know have a 1 minute break.\nThe next block will automatically start after it.\n\n**To skip this break, press any key.**',
        font='Arial',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0,
        color='white', colorSpace='rgb', opacity=1,
        languageStyle='LTR',
        depth=0.0);
    end_break = keyboard.Keyboard()

    # Initialize components for Routine "feedback"
    feedbackClock = core.Clock()
    end_text = visual.TextStim(win=win, name='end_text',
        text='The experiment is now over. Thank you for your participation.\n\nTo find your results, go to the place where the experiment is saved.\nThere should be a folder created called "data" where you will be able to find a csv file with your results.\n\nPress any key to exit this screen.',
        font='Arial',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0,
        color='white', colorSpace='rgb', opacity=1,
        languageStyle='LTR',
        depth=0.0);
    end_experiment = keyboard.Keyboard()

    # Create some handy timers
    globalClock = core.Clock()  # to track the time since experiment started
    routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine

    # ------Prepare to start Routine "instructionsText"-------
    continueRoutine = True
    # update component parameters for each repeat
    next_instructions.keys = []
    next_instructions.rt = []
    _next_instructions_allKeys = []
    # keep track of which components have finished
    instructionsTextComponents = [instructions, next_instructions]
    for thisComponent in instructionsTextComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instructionsTextClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "instructionsText"-------
    while continueRoutine:
        # get current time
        t = instructionsTextClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instructionsTextClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *instructions* updates
        if instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructions.frameNStart = frameN  # exact frame index
            instructions.tStart = t  # local t and not account for scr refresh
            instructions.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructions, 'tStartRefresh')  # time at next scr refresh
            instructions.setAutoDraw(True)

        # *next_instructions* updates
        waitOnFlip = False
        if next_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            next_instructions.frameNStart = frameN  # exact frame index
            next_instructions.tStart = t  # local t and not account for scr refresh
            next_instructions.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(next_instructions, 'tStartRefresh')  # time at next scr refresh
            next_instructions.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(next_instructions.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(next_instructions.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if next_instructions.status == STARTED and not waitOnFlip:
            theseKeys = next_instructions.getKeys(keyList=['space'], waitRelease=False)
            _next_instructions_allKeys.extend(theseKeys)
            if len(_next_instructions_allKeys):
                next_instructions.keys = _next_instructions_allKeys[-1].name  # just the last key pressed
                next_instructions.rt = _next_instructions_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructionsTextComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "instructionsText"-------
    for thisComponent in instructionsTextComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('instructions.started', instructions.tStartRefresh)
    thisExp.addData('instructions.stopped', instructions.tStopRefresh)
    # the Routine "instructionsText" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    # ------Prepare to start Routine "instructionsText2"-------
    continueRoutine = True
    # update component parameters for each repeat
    begin_experiment.keys = []
    begin_experiment.rt = []
    _begin_experiment_allKeys = []
    # keep track of which components have finished
    instructionsText2Components = [for_example, red, begin_experiment, press_r]
    for thisComponent in instructionsText2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instructionsText2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # Start the EEG recording

    # -------Run Routine "instructionsText2"-------
    while continueRoutine:
        # get current time
        t = instructionsText2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instructionsText2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *for_example* updates
        if for_example.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            for_example.frameNStart = frameN  # exact frame index
            for_example.tStart = t  # local t and not account for scr refresh
            for_example.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(for_example, 'tStartRefresh')  # time at next scr refresh
            for_example.setAutoDraw(True)

        # *red* updates
        if red.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            red.frameNStart = frameN  # exact frame index
            red.tStart = t  # local t and not account for scr refresh
            red.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(red, 'tStartRefresh')  # time at next scr refresh
            red.setAutoDraw(True)

        # *begin_experiment* updates
        waitOnFlip = False
        if begin_experiment.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            begin_experiment.frameNStart = frameN  # exact frame index
            begin_experiment.tStart = t  # local t and not account for scr refresh
            begin_experiment.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(begin_experiment, 'tStartRefresh')  # time at next scr refresh
            begin_experiment.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(begin_experiment.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(begin_experiment.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if begin_experiment.status == STARTED and not waitOnFlip:
            theseKeys = begin_experiment.getKeys(keyList=None, waitRelease=False)
            _begin_experiment_allKeys.extend(theseKeys)
            if len(_begin_experiment_allKeys):
                begin_experiment.keys = _begin_experiment_allKeys[-1].name  # just the last key pressed
                begin_experiment.rt = _begin_experiment_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False

        # *press_r* updates
        if press_r.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            press_r.frameNStart = frameN  # exact frame index
            press_r.tStart = t  # local t and not account for scr refresh
            press_r.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(press_r, 'tStartRefresh')  # time at next scr refresh
            press_r.setAutoDraw(True)

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructionsText2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "instructionsText2"-------
    for thisComponent in instructionsText2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('for_example.started', for_example.tStartRefresh)
    thisExp.addData('for_example.stopped', for_example.tStopRefresh)
    thisExp.addData('red.started', red.tStartRefresh)
    thisExp.addData('red.stopped', red.tStopRefresh)
    # check responses
    if begin_experiment.keys in ['', [], None]:  # No response was made
        begin_experiment.keys = None
    thisExp.addData('begin_experiment.keys',begin_experiment.keys)
    if begin_experiment.keys != None:  # we had a response
        thisExp.addData('begin_experiment.rt', begin_experiment.rt)
    thisExp.addData('begin_experiment.started', begin_experiment.tStartRefresh)
    thisExp.addData('begin_experiment.stopped', begin_experiment.tStopRefresh)
    thisExp.nextEntry()
    thisExp.addData('press_r.started', press_r.tStartRefresh)
    thisExp.addData('press_r.stopped', press_r.tStopRefresh)
    # the Routine "instructionsText2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    # set up handler to look after randomisation of conditions etc
    block_1 = data.TrialHandler(nReps=1, method='random',
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(_thisDir + os.sep + 'conditionsStroop.xlsx'),
        seed=None, name='block_1')
    thisExp.addLoop(block_1)  # add the loop to the experiment
    thisBlock_1 = block_1.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBlock_1.rgb)
    #if thisBlock_1 != None:
    #    for paramName in thisBlock_1:
    #        exec('{} = thisBlock_1[paramName]'.format(paramName))

    for thisBlock_1 in block_1:
        # abbreviate parameter names if possible (e.g. rgb = thisBlock_1.rgb)
        #if thisBlock_1 != None:
        #    for paramName in thisBlock_1:
        #        exec('{} = thisBlock_1[paramName]'.format(paramName))
        currentLoop = block_1
        stroop.setColor(thisBlock_1["colour"], colorSpace='rgb')
        stroop.setText(thisBlock_1["word"])
        # ------Prepare to start Routine "trial"-------
        continueRoutine = True
        # get initial time
        init = trialClock.getTime()
        # update component parameters for each repeat
        response.keys = []
        response.rt = []
        _response_allKeys = []
        # keep track of which components have finished
        trialComponents = [stroop, response]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1

        # -------Run Routine "trial"-------
        while continueRoutine:
            # get current time at each moment
            t = trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame

            # *stroop* updates
            if stroop.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                stroop.frameNStart = frameN  # exact frame index
                stroop.tStart = t  # local t and not account for scr refresh
                stroop.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stroop, 'tStartRefresh')  # time at next scr refresh
                stroop.setAutoDraw(True)

            if stroop.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > stroop.tStartRefresh + 10-frameTolerance:
                    # keep track of stop time/frame for later
                    stroop.tStop = t  # not accounting for scr refresh
                    stroop.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(stroop, 'tStopRefresh')  # time at next scr refresh
                    stroop.setAutoDraw(False)

            # *response* updates
            waitOnFlip = False
            if response.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                response.frameNStart = frameN  # exact frame index
                response.tStart = t  # local t and not account for scr refresh
                response.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(response, 'tStartRefresh')  # time at next scr refresh
                response.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(response.clock.reset)  # t=0 on next screen flip
                if response.status == NOT_STARTED and t-init >= 5:  ## This section should quit the trial if no key press after 5 s but doesn't work :(
                    continueRoutine = False

            if response.status == STARTED and not waitOnFlip:
                theseKeys = response.getKeys(keyList=['r', 'g', 'b', 'y'], waitRelease=False)
                _response_allKeys.extend(theseKeys)
                if len(_response_allKeys):
                    response.keys = _response_allKeys[-1].name  # just the last key pressed
                    response.rt = _response_allKeys[-1].rt
                    # was this correct?
                    if (response.keys == str(thisBlock_1["corrAns"])) or (response.keys == thisBlock_1["corrAns"]):
                        response.corr = 1
                    else:
                        response.corr = 0
                    # a response ends the routine
                    continueRoutine = False

            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()

            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished

            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        block_1.addData('stroop.started', stroop.tStartRefresh)
        block_1.addData('stroop.stopped', stroop.tStopRefresh)
        # check responses
        if response.keys in ['', [], None]:  # No response was made
            response.keys = None
            # was no response the correct answer?!
            if str(thisBlock_1["corrAns"]).lower() == 'none':
               response.corr = 1;  # correct non-response
            else:
               response.corr = 0;  # failed to respond (incorrectly)
        # store data for block_1 (TrialHandler)
        block_1.addData('response.keys',response.keys)
        block_1.addData('response.corr', response.corr)
        if response.keys != None:  # we had a response
            block_1.addData('response.rt', response.rt)
        block_1.addData('response.started', response.tStartRefresh)
        block_1.addData('response.stopped', response.tStopRefresh)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()

    # completed 1 repeats of 'block_1'


    # ------Prepare to start Routine "break_2"-------
    continueRoutine = True
    routineTimer.add(60.000000)
    # update component parameters for each repeat
    end_break.keys = []
    end_break.rt = []
    _end_break_allKeys = []
    # keep track of which components have finished
    break_2Components = [break_instructions, end_break]
    for thisComponent in break_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    break_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "break_2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = break_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=break_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *break_instructions* updates
        if break_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            break_instructions.frameNStart = frameN  # exact frame index
            break_instructions.tStart = t  # local t and not account for scr refresh
            break_instructions.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(break_instructions, 'tStartRefresh')  # time at next scr refresh
            break_instructions.setAutoDraw(True)
        if break_instructions.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > break_instructions.tStartRefresh + 60-frameTolerance:
                # keep track of stop time/frame for later
                break_instructions.tStop = t  # not accounting for scr refresh
                break_instructions.frameNStop = frameN  # exact frame index
                win.timeOnFlip(break_instructions, 'tStopRefresh')  # time at next scr refresh
                break_instructions.setAutoDraw(False)

        # *end_break* updates
        waitOnFlip = False
        if end_break.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            end_break.frameNStart = frameN  # exact frame index
            end_break.tStart = t  # local t and not account for scr refresh
            end_break.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(end_break, 'tStartRefresh')  # time at next scr refresh
            end_break.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(end_break.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(end_break.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if end_break.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > end_break.tStartRefresh + 60-frameTolerance:
                # keep track of stop time/frame for later
                end_break.tStop = t  # not accounting for scr refresh
                end_break.frameNStop = frameN  # exact frame index
                win.timeOnFlip(end_break, 'tStopRefresh')  # time at next scr refresh
                end_break.status = FINISHED
        if end_break.status == STARTED and not waitOnFlip:
            theseKeys = end_break.getKeys(keyList=None, waitRelease=False)
            _end_break_allKeys.extend(theseKeys)
            if len(_end_break_allKeys):
                end_break.keys = _end_break_allKeys[-1].name  # just the last key pressed
                end_break.rt = _end_break_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in break_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "break_2"-------
    for thisComponent in break_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('break_instructions.started', break_instructions.tStartRefresh)
    thisExp.addData('break_instructions.stopped', break_instructions.tStopRefresh)

    # set up handler to look after randomisation of conditions etc
    block_2 = data.TrialHandler(nReps=1, method='random',
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('conditionsStroop2.xlsx'),
        seed=None, name='block_2')
    thisExp.addLoop(block_2)  # add the loop to the experiment
    thisBlock_2 = block_2.trialList[0]  # so we can initialise stimuli with some values

    for thisBlock_2 in block_2:
        currentLoop = block_2

        # ------Prepare to start Routine "trial"-------
        continueRoutine = True
        # update component parameters for each repeat
        stroop.setColor(thisBlock_2["colour"], colorSpace='rgb')
        stroop.setText(thisBlock_2["word"])
        response.keys = []
        response.rt = []
        _response_allKeys = []
        # keep track of which components have finished
        trialComponents = [stroop, response]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1

        # -------Run Routine "trial"-------
        while continueRoutine:
            # get current time
            t = trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame

            # *stroop* updates
            if stroop.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                stroop.frameNStart = frameN  # exact frame index
                stroop.tStart = t  # local t and not account for scr refresh
                stroop.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stroop, 'tStartRefresh')  # time at next scr refresh
                stroop.setAutoDraw(True)
            if stroop.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > stroop.tStartRefresh + 10-frameTolerance:
                    # keep track of stop time/frame for later
                    stroop.tStop = t  # not accounting for scr refresh
                    stroop.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(stroop, 'tStopRefresh')  # time at next scr refresh
                    stroop.setAutoDraw(False)

            # *response* updates
            waitOnFlip = False
            if response.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                response.frameNStart = frameN  # exact frame index
                response.tStart = t  # local t and not account for scr refresh
                response.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(response, 'tStartRefresh')  # time at next scr refresh
                response.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(response.clock.reset)  # t=0 on next screen flip
            if response.status == STARTED and not waitOnFlip:
                theseKeys = response.getKeys(keyList=['r', 'g', 'b', 'y'], waitRelease=False)
                _response_allKeys.extend(theseKeys)
                if len(_response_allKeys):
                    response.keys = _response_allKeys[-1].name  # just the last key pressed
                    response.rt = _response_allKeys[-1].rt
                    # was this correct?
                    if (response.keys == str(thisBlock_2["corrAns"])) or (response.keys == thisBlock_2["corrAns"]):
                        response.corr = 1
                    else:
                        response.corr = 0
                    # a response ends the routine
                    continueRoutine = False

            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()

            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished

            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        block_2.addData('stroop.started', stroop.tStartRefresh)
        block_2.addData('stroop.stopped', stroop.tStopRefresh)
        # check responses
        if response.keys in ['', [], None]:  # No response was made
            response.keys = None
            # was no response the correct answer?!
            if str(thisBlock_2["corrAns"]).lower() == 'none':
               response.corr = 1;  # correct non-response
            else:
               response.corr = 0;  # failed to respond (incorrectly)
        # store data for block_2 (TrialHandler)
        block_2.addData('response.keys',response.keys)
        block_2.addData('response.corr', response.corr)
        if response.keys != None:  # we had a response
            block_2.addData('response.rt', response.rt)
        block_2.addData('response.started', response.tStartRefresh)
        block_2.addData('response.stopped', response.tStopRefresh)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()

    # completed 1 repeats of 'block_2'


    # ------Prepare to start Routine "break_2"-------
    continueRoutine = True
    routineTimer.add(60.000000)
    # update component parameters for each repeat
    end_break.keys = []
    end_break.rt = []
    _end_break_allKeys = []
    # keep track of which components have finished
    break_2Components = [break_instructions, end_break]
    for thisComponent in break_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    break_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "break_2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = break_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=break_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *break_instructions* updates
        if break_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            break_instructions.frameNStart = frameN  # exact frame index
            break_instructions.tStart = t  # local t and not account for scr refresh
            break_instructions.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(break_instructions, 'tStartRefresh')  # time at next scr refresh
            break_instructions.setAutoDraw(True)
        if break_instructions.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > break_instructions.tStartRefresh + 60-frameTolerance:
                # keep track of stop time/frame for later
                break_instructions.tStop = t  # not accounting for scr refresh
                break_instructions.frameNStop = frameN  # exact frame index
                win.timeOnFlip(break_instructions, 'tStopRefresh')  # time at next scr refresh
                break_instructions.setAutoDraw(False)

        # *end_break* updates
        waitOnFlip = False
        if end_break.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            end_break.frameNStart = frameN  # exact frame index
            end_break.tStart = t  # local t and not account for scr refresh
            end_break.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(end_break, 'tStartRefresh')  # time at next scr refresh
            end_break.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(end_break.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(end_break.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if end_break.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > end_break.tStartRefresh + 60-frameTolerance:
                # keep track of stop time/frame for later
                end_break.tStop = t  # not accounting for scr refresh
                end_break.frameNStop = frameN  # exact frame index
                win.timeOnFlip(end_break, 'tStopRefresh')  # time at next scr refresh
                end_break.status = FINISHED
        if end_break.status == STARTED and not waitOnFlip:
            theseKeys = end_break.getKeys(keyList=None, waitRelease=False)
            _end_break_allKeys.extend(theseKeys)
            if len(_end_break_allKeys):
                end_break.keys = _end_break_allKeys[-1].name  # just the last key pressed
                end_break.rt = _end_break_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in break_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "break_2"-------
    for thisComponent in break_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('break_instructions.started', break_instructions.tStartRefresh)
    thisExp.addData('break_instructions.stopped', break_instructions.tStopRefresh)

    # set up handler to look after randomisation of conditions etc
    block_3 = data.TrialHandler(nReps=1, method='random',
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('conditionsStroop.xlsx'),
        seed=None, name='block_3')
    thisExp.addLoop(block_3)  # add the loop to the experiment
    thisBlock_3 = block_3.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBlock_3.rgb)
    #if thisBlock_3 != None:
    #    for paramName in thisBlock_3:
    #        exec('{} = thisBlock_3[paramName]'.format(paramName))

    for thisBlock_3 in block_3:
        currentLoop = block_3
        # abbreviate parameter names if possible (e.g. rgb = thisBlock_3.rgb)
        #if thisBlock_3 != None:
        #    for paramName in thisBlock_3:
        #        exec('{} = thisBlock_3[paramName]'.format(paramName))

        # ------Prepare to start Routine "trial"-------
        continueRoutine = True
        # update component parameters for each repeat
        stroop.setColor(thisBlock_3["colour"], colorSpace='rgb')
        stroop.setText(thisBlock_3["word"])
        response.keys = []
        response.rt = []
        _response_allKeys = []
        # keep track of which components have finished
        trialComponents = [stroop, response]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1

        # -------Run Routine "trial"-------
        while continueRoutine:
            # get current time
            t = trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame

            # *stroop* updates
            if stroop.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                stroop.frameNStart = frameN  # exact frame index
                stroop.tStart = t  # local t and not account for scr refresh
                stroop.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stroop, 'tStartRefresh')  # time at next scr refresh
                stroop.setAutoDraw(True)
            if stroop.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > stroop.tStartRefresh + 10-frameTolerance:
                    # keep track of stop time/frame for later
                    stroop.tStop = t  # not accounting for scr refresh
                    stroop.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(stroop, 'tStopRefresh')  # time at next scr refresh
                    stroop.setAutoDraw(False)

            # *response* updates
            waitOnFlip = False
            if response.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                response.frameNStart = frameN  # exact frame index
                response.tStart = t  # local t and not account for scr refresh
                response.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(response, 'tStartRefresh')  # time at next scr refresh
                response.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(response.clock.reset)  # t=0 on next screen flip
            if response.status == STARTED and not waitOnFlip:
                theseKeys = response.getKeys(keyList=['r', 'g', 'b', 'y'], waitRelease=False)
                _response_allKeys.extend(theseKeys)
                if len(_response_allKeys):
                    response.keys = _response_allKeys[-1].name  # just the last key pressed
                    response.rt = _response_allKeys[-1].rt
                    # was this correct?
                    if (response.keys == str(thisBlock_3["corrAns"])) or (response.keys == thisBlock_3["corrAns"]):
                        response.corr = 1
                    else:
                        response.corr = 0
                    # a response ends the routine
                    continueRoutine = False

            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()

            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished

            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        block_3.addData('stroop.started', stroop.tStartRefresh)
        block_3.addData('stroop.stopped', stroop.tStopRefresh)
        # check responses
        if response.keys in ['', [], None]:  # No response was made
            response.keys = None
            # was no response the correct answer?!
            if str(thisBlock_3["corrAns"]).lower() == 'none':
               response.corr = 1;  # correct non-response
            else:
               response.corr = 0;  # failed to respond (incorrectly)
        # store data for block_3 (TrialHandler)
        block_3.addData('response.keys',response.keys)
        block_3.addData('response.corr', response.corr)
        if response.keys != None:  # we had a response
            block_3.addData('response.rt', response.rt)
        block_3.addData('response.started', response.tStartRefresh)
        block_3.addData('response.stopped', response.tStopRefresh)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()

    # completed 1 repeats of 'block_3'


    # ------Prepare to start Routine "break_2"-------
    continueRoutine = True
    routineTimer.add(60.000000)
    # update component parameters for each repeat
    end_break.keys = []
    end_break.rt = []
    _end_break_allKeys = []
    # keep track of which components have finished
    break_2Components = [break_instructions, end_break]
    for thisComponent in break_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    break_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "break_2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = break_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=break_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *break_instructions* updates
        if break_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            break_instructions.frameNStart = frameN  # exact frame index
            break_instructions.tStart = t  # local t and not account for scr refresh
            break_instructions.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(break_instructions, 'tStartRefresh')  # time at next scr refresh
            break_instructions.setAutoDraw(True)
        if break_instructions.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > break_instructions.tStartRefresh + 60-frameTolerance:
                # keep track of stop time/frame for later
                break_instructions.tStop = t  # not accounting for scr refresh
                break_instructions.frameNStop = frameN  # exact frame index
                win.timeOnFlip(break_instructions, 'tStopRefresh')  # time at next scr refresh
                break_instructions.setAutoDraw(False)

        # *end_break* updates
        waitOnFlip = False
        if end_break.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            end_break.frameNStart = frameN  # exact frame index
            end_break.tStart = t  # local t and not account for scr refresh
            end_break.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(end_break, 'tStartRefresh')  # time at next scr refresh
            end_break.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(end_break.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(end_break.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if end_break.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > end_break.tStartRefresh + 60-frameTolerance:
                # keep track of stop time/frame for later
                end_break.tStop = t  # not accounting for scr refresh
                end_break.frameNStop = frameN  # exact frame index
                win.timeOnFlip(end_break, 'tStopRefresh')  # time at next scr refresh
                end_break.status = FINISHED
        if end_break.status == STARTED and not waitOnFlip:
            theseKeys = end_break.getKeys(keyList=None, waitRelease=False)
            _end_break_allKeys.extend(theseKeys)
            if len(_end_break_allKeys):
                end_break.keys = _end_break_allKeys[-1].name  # just the last key pressed
                end_break.rt = _end_break_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in break_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "break_2"-------
    for thisComponent in break_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('break_instructions.started', break_instructions.tStartRefresh)
    thisExp.addData('break_instructions.stopped', break_instructions.tStopRefresh)

    # set up handler to look after randomisation of conditions etc
    block_4 = data.TrialHandler(nReps=1, method='random',
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('conditionsStroop2.xlsx'),
        seed=None, name='block_4')
    thisExp.addLoop(block_4)  # add the loop to the experiment
    thisBlock_4 = block_4.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBlock_4.rgb)
    #if thisBlock_4 != None:
    #    for paramName in thisBlock_4:
    #        exec('{} = thisBlock_4[paramName]'.format(paramName))

    for thisBlock_4 in block_4:
        currentLoop = block_4
        # abbreviate parameter names if possible (e.g. rgb = thisBlock_4.rgb)
        #if thisBlock_4 != None:
        #    for paramName in thisBlock_4:
        #        exec('{} = thisBlock_4[paramName]'.format(paramName))

        # ------Prepare to start Routine "trial"-------
        continueRoutine = True
        # update component parameters for each repeat
        stroop.setColor(thisBlock_4["colour"], colorSpace='rgb')
        stroop.setText(thisBlock_4["word"])
        response.keys = []
        response.rt = []
        _response_allKeys = []
        # keep track of which components have finished
        trialComponents = [stroop, response]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1

        # -------Run Routine "trial"-------
        while continueRoutine:
            # get current time
            t = trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame

            # *stroop* updates
            if stroop.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                stroop.frameNStart = frameN  # exact frame index
                stroop.tStart = t  # local t and not account for scr refresh
                stroop.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stroop, 'tStartRefresh')  # time at next scr refresh
                stroop.setAutoDraw(True)
            if stroop.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > stroop.tStartRefresh + 10-frameTolerance:
                    # keep track of stop time/frame for later
                    stroop.tStop = t  # not accounting for scr refresh
                    stroop.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(stroop, 'tStopRefresh')  # time at next scr refresh
                    stroop.setAutoDraw(False)

            # *response* updates
            waitOnFlip = False
            if response.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                response.frameNStart = frameN  # exact frame index
                response.tStart = t  # local t and not account for scr refresh
                response.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(response, 'tStartRefresh')  # time at next scr refresh
                response.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(response.clock.reset)  # t=0 on next screen flip
            if response.status == STARTED and not waitOnFlip:
                theseKeys = response.getKeys(keyList=['r', 'g', 'b', 'y'], waitRelease=False)
                _response_allKeys.extend(theseKeys)
                if len(_response_allKeys):
                    response.keys = _response_allKeys[-1].name  # just the last key pressed
                    response.rt = _response_allKeys[-1].rt
                    # was this correct?
                    if (response.keys == str(thisBlock_4["corrAns"])) or (response.keys == thisBlock_4["corrAns"]):
                        response.corr = 1
                    else:
                        response.corr = 0
                    # a response ends the routine
                    continueRoutine = False

            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()

            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished

            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        block_4.addData('stroop.started', stroop.tStartRefresh)
        block_4.addData('stroop.stopped', stroop.tStopRefresh)
        # check responses
        if response.keys in ['', [], None]:  # No response was made
            response.keys = None
            # was no response the correct answer?!
            if str(thisBlock_4["corrAns"]).lower() == 'none':
               response.corr = 1;  # correct non-response
            else:
               response.corr = 0;  # failed to respond (incorrectly)
        # store data for block_4 (TrialHandler)
        block_4.addData('response.keys',response.keys)
        block_4.addData('response.corr', response.corr)
        if response.keys != None:  # we had a response
            block_4.addData('response.rt', response.rt)
        block_4.addData('response.started', response.tStartRefresh)
        block_4.addData('response.stopped', response.tStopRefresh)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()

    # completed 1 repeats of 'block_4'


    # ------Prepare to start Routine "break_2"-------
    continueRoutine = True
    routineTimer.add(60.000000)
    # update component parameters for each repeat
    end_break.keys = []
    end_break.rt = []
    _end_break_allKeys = []
    # keep track of which components have finished
    break_2Components = [break_instructions, end_break]
    for thisComponent in break_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    break_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "break_2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = break_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=break_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *break_instructions* updates
        if break_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            break_instructions.frameNStart = frameN  # exact frame index
            break_instructions.tStart = t  # local t and not account for scr refresh
            break_instructions.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(break_instructions, 'tStartRefresh')  # time at next scr refresh
            break_instructions.setAutoDraw(True)
        if break_instructions.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > break_instructions.tStartRefresh + 60-frameTolerance:
                # keep track of stop time/frame for later
                break_instructions.tStop = t  # not accounting for scr refresh
                break_instructions.frameNStop = frameN  # exact frame index
                win.timeOnFlip(break_instructions, 'tStopRefresh')  # time at next scr refresh
                break_instructions.setAutoDraw(False)

        # *end_break* updates
        waitOnFlip = False
        if end_break.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            end_break.frameNStart = frameN  # exact frame index
            end_break.tStart = t  # local t and not account for scr refresh
            end_break.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(end_break, 'tStartRefresh')  # time at next scr refresh
            end_break.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(end_break.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(end_break.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if end_break.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > end_break.tStartRefresh + 60-frameTolerance:
                # keep track of stop time/frame for later
                end_break.tStop = t  # not accounting for scr refresh
                end_break.frameNStop = frameN  # exact frame index
                win.timeOnFlip(end_break, 'tStopRefresh')  # time at next scr refresh
                end_break.status = FINISHED
        if end_break.status == STARTED and not waitOnFlip:
            theseKeys = end_break.getKeys(keyList=None, waitRelease=False)
            _end_break_allKeys.extend(theseKeys)
            if len(_end_break_allKeys):
                end_break.keys = _end_break_allKeys[-1].name  # just the last key pressed
                end_break.rt = _end_break_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in break_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "break_2"-------
    for thisComponent in break_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('break_instructions.started', break_instructions.tStartRefresh)
    thisExp.addData('break_instructions.stopped', break_instructions.tStopRefresh)

    # set up handler to look after randomisation of conditions etc
    block_5 = data.TrialHandler(nReps=1, method='random',
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('conditionsStroop.xlsx'),
        seed=None, name='block_5')
    thisExp.addLoop(block_5)  # add the loop to the experiment
    thisBlock_5 = block_5.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBlock_5.rgb)
    #if thisBlock_5 != None:
    #    for paramName in thisBlock_5:
    #        exec('{} = thisBlock_5[paramName]'.format(paramName))

    for thisBlock_5 in block_5:
        currentLoop = block_5
        # abbreviate parameter names if possible (e.g. rgb = thisBlock_5.rgb)
        #if thisBlock_5 != None:
        #    for paramName in thisBlock_5:
        #        exec('{} = thisBlock_5[paramName]'.format(paramName))

        # ------Prepare to start Routine "trial"-------
        continueRoutine = True
        # update component parameters for each repeat
        stroop.setColor(thisBlock_5["colour"], colorSpace='rgb')
        stroop.setText(thisBlock_5["word"])
        response.keys = []
        response.rt = []
        _response_allKeys = []
        # keep track of which components have finished
        trialComponents = [stroop, response]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1

        # -------Run Routine "trial"-------
        while continueRoutine:
            # get current time
            t = trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame

            # *stroop* updates
            if stroop.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                stroop.frameNStart = frameN  # exact frame index
                stroop.tStart = t  # local t and not account for scr refresh
                stroop.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stroop, 'tStartRefresh')  # time at next scr refresh
                stroop.setAutoDraw(True)
            if stroop.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > stroop.tStartRefresh + 10-frameTolerance:
                    # keep track of stop time/frame for later
                    stroop.tStop = t  # not accounting for scr refresh
                    stroop.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(stroop, 'tStopRefresh')  # time at next scr refresh
                    stroop.setAutoDraw(False)

            # *response* updates
            waitOnFlip = False
            if response.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                response.frameNStart = frameN  # exact frame index
                response.tStart = t  # local t and not account for scr refresh
                response.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(response, 'tStartRefresh')  # time at next scr refresh
                response.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(response.clock.reset)  # t=0 on next screen flip
            if response.status == STARTED and not waitOnFlip:
                theseKeys = response.getKeys(keyList=['r', 'g', 'b', 'y'], waitRelease=False)
                _response_allKeys.extend(theseKeys)
                if len(_response_allKeys):
                    response.keys = _response_allKeys[-1].name  # just the last key pressed
                    response.rt = _response_allKeys[-1].rt
                    # was this correct?
                    if (response.keys == str(thisBlock_5["corrAns"])) or (response.keys == thisBlock_5["corrAns"]):
                        response.corr = 1
                    else:
                        response.corr = 0
                    # a response ends the routine
                    continueRoutine = False

            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()

            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished

            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        block_5.addData('stroop.started', stroop.tStartRefresh)
        block_5.addData('stroop.stopped', stroop.tStopRefresh)
        # check responses
        if response.keys in ['', [], None]:  # No response was made
            response.keys = None
            # was no response the correct answer?!
            if str(thisBlock_5["corrAns"]).lower() == 'none':
               response.corr = 1;  # correct non-response
            else:
               response.corr = 0;  # failed to respond (incorrectly)
        # store data for block_5 (TrialHandler)
        block_5.addData('response.keys',response.keys)
        block_5.addData('response.corr', response.corr)
        if response.keys != None:  # we had a response
            block_5.addData('response.rt', response.rt)
        block_5.addData('response.started', response.tStartRefresh)
        block_5.addData('response.stopped', response.tStopRefresh)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()

    # completed 1 repeats of 'block_5'


    # ------Prepare to start Routine "break_2"-------
    continueRoutine = True
    routineTimer.add(60.000000)
    # update component parameters for each repeat
    end_break.keys = []
    end_break.rt = []
    _end_break_allKeys = []
    # keep track of which components have finished
    break_2Components = [break_instructions, end_break]
    for thisComponent in break_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    break_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "break_2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = break_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=break_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *break_instructions* updates
        if break_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            break_instructions.frameNStart = frameN  # exact frame index
            break_instructions.tStart = t  # local t and not account for scr refresh
            break_instructions.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(break_instructions, 'tStartRefresh')  # time at next scr refresh
            break_instructions.setAutoDraw(True)
        if break_instructions.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > break_instructions.tStartRefresh + 60-frameTolerance:
                # keep track of stop time/frame for later
                break_instructions.tStop = t  # not accounting for scr refresh
                break_instructions.frameNStop = frameN  # exact frame index
                win.timeOnFlip(break_instructions, 'tStopRefresh')  # time at next scr refresh
                break_instructions.setAutoDraw(False)

        # *end_break* updates
        waitOnFlip = False
        if end_break.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            end_break.frameNStart = frameN  # exact frame index
            end_break.tStart = t  # local t and not account for scr refresh
            end_break.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(end_break, 'tStartRefresh')  # time at next scr refresh
            end_break.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(end_break.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(end_break.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if end_break.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > end_break.tStartRefresh + 60-frameTolerance:
                # keep track of stop time/frame for later
                end_break.tStop = t  # not accounting for scr refresh
                end_break.frameNStop = frameN  # exact frame index
                win.timeOnFlip(end_break, 'tStopRefresh')  # time at next scr refresh
                end_break.status = FINISHED
        if end_break.status == STARTED and not waitOnFlip:
            theseKeys = end_break.getKeys(keyList=None, waitRelease=False)
            _end_break_allKeys.extend(theseKeys)
            if len(_end_break_allKeys):
                end_break.keys = _end_break_allKeys[-1].name  # just the last key pressed
                end_break.rt = _end_break_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in break_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "break_2"-------
    for thisComponent in break_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('break_instructions.started', break_instructions.tStartRefresh)
    thisExp.addData('break_instructions.stopped', break_instructions.tStopRefresh)

    # set up handler to look after randomisation of conditions etc
    block_6 = data.TrialHandler(nReps=1, method='random',
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('conditionsStroop2.xlsx'),
        seed=None, name='block_6')
    thisExp.addLoop(block_6)  # add the loop to the experiment
    thisBlock_6 = block_6.trialList[0]  # so we can initialise stimuli with some values

    for thisBlock_6 in block_6:
        currentLoop = block_6

        # ------Prepare to start Routine "trial"-------
        continueRoutine = True
        # update component parameters for each repeat
        stroop.setColor(thisBlock_6["colour"], colorSpace='rgb')
        stroop.setText(thisBlock_6["word"])
        response.keys = []
        response.rt = []
        _response_allKeys = []
        # keep track of which components have finished
        trialComponents = [stroop, response]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1

        # -------Run Routine "trial"-------
        while continueRoutine:
            # get current time
            t = trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame

            # *stroop* updates
            if stroop.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                stroop.frameNStart = frameN  # exact frame index
                stroop.tStart = t  # local t and not account for scr refresh
                stroop.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stroop, 'tStartRefresh')  # time at next scr refresh
                stroop.setAutoDraw(True)
            if stroop.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > stroop.tStartRefresh + 10-frameTolerance:
                    # keep track of stop time/frame for later
                    stroop.tStop = t  # not accounting for scr refresh
                    stroop.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(stroop, 'tStopRefresh')  # time at next scr refresh
                    stroop.setAutoDraw(False)

            # *response* updates
            waitOnFlip = False
            if response.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                response.frameNStart = frameN  # exact frame index
                response.tStart = t  # local t and not account for scr refresh
                response.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(response, 'tStartRefresh')  # time at next scr refresh
                response.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(response.clock.reset)  # t=0 on next screen flip
            if response.status == STARTED and not waitOnFlip:
                theseKeys = response.getKeys(keyList=['r', 'g', 'b', 'y'], waitRelease=False)
                _response_allKeys.extend(theseKeys)
                if len(_response_allKeys):
                    response.keys = _response_allKeys[-1].name  # just the last key pressed
                    response.rt = _response_allKeys[-1].rt
                    # was this correct?
                    if (response.keys == str(thisBlock_6["corrAns"])) or (response.keys == thisBlock_6["corrAns"]):
                        response.corr = 1
                    else:
                        response.corr = 0
                    # a response ends the routine
                    continueRoutine = False

            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()

            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished

            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        block_6.addData('stroop.started', stroop.tStartRefresh)
        block_6.addData('stroop.stopped', stroop.tStopRefresh)
        # check responses
        if response.keys in ['', [], None]:  # No response was made
            response.keys = None
            # was no response the correct answer?!
            if str(corrAns).lower() == 'none':
               response.corr = 1;  # correct non-response
            else:
               response.corr = 0;  # failed to respond (incorrectly)
        # store data for block_6 (TrialHandler)
        block_6.addData('response.keys',response.keys)
        block_6.addData('response.corr', response.corr)
        if response.keys != None:  # we had a response
            block_6.addData('response.rt', response.rt)
        block_6.addData('response.started', response.tStartRefresh)
        block_6.addData('response.stopped', response.tStopRefresh)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()

    # completed 1 repeats of 'block_6'


    # ------Prepare to start Routine "break_2"-------
    continueRoutine = True
    routineTimer.add(60.000000)
    # update component parameters for each repeat
    end_break.keys = []
    end_break.rt = []
    _end_break_allKeys = []
    # keep track of which components have finished
    break_2Components = [break_instructions, end_break]
    for thisComponent in break_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    break_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "break_2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = break_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=break_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *break_instructions* updates
        if break_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            break_instructions.frameNStart = frameN  # exact frame index
            break_instructions.tStart = t  # local t and not account for scr refresh
            break_instructions.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(break_instructions, 'tStartRefresh')  # time at next scr refresh
            break_instructions.setAutoDraw(True)
        if break_instructions.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > break_instructions.tStartRefresh + 60-frameTolerance:
                # keep track of stop time/frame for later
                break_instructions.tStop = t  # not accounting for scr refresh
                break_instructions.frameNStop = frameN  # exact frame index
                win.timeOnFlip(break_instructions, 'tStopRefresh')  # time at next scr refresh
                break_instructions.setAutoDraw(False)

        # *end_break* updates
        waitOnFlip = False
        if end_break.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            end_break.frameNStart = frameN  # exact frame index
            end_break.tStart = t  # local t and not account for scr refresh
            end_break.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(end_break, 'tStartRefresh')  # time at next scr refresh
            end_break.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(end_break.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(end_break.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if end_break.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > end_break.tStartRefresh + 60-frameTolerance:
                # keep track of stop time/frame for later
                end_break.tStop = t  # not accounting for scr refresh
                end_break.frameNStop = frameN  # exact frame index
                win.timeOnFlip(end_break, 'tStopRefresh')  # time at next scr refresh
                end_break.status = FINISHED
        if end_break.status == STARTED and not waitOnFlip:
            theseKeys = end_break.getKeys(keyList=None, waitRelease=False)
            _end_break_allKeys.extend(theseKeys)
            if len(_end_break_allKeys):
                end_break.keys = _end_break_allKeys[-1].name  # just the last key pressed
                end_break.rt = _end_break_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in break_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "break_2"-------
    for thisComponent in break_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('break_instructions.started', break_instructions.tStartRefresh)
    thisExp.addData('break_instructions.stopped', break_instructions.tStopRefresh)

    # set up handler to look after randomisation of conditions etc
    block_7 = data.TrialHandler(nReps=1, method='random',
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('conditionsStroop.xlsx'),
        seed=None, name='block_7')
    thisExp.addLoop(block_7)  # add the loop to the experiment
    thisBlock_7 = block_7.trialList[0]  # so we can initialise stimuli with some values

    for thisBlock_7 in block_7:
        currentLoop = block_7

        # ------Prepare to start Routine "trial"-------
        continueRoutine = True
        # update component parameters for each repeat
        stroop.setColor(thisBlock_7["colour"], colorSpace='rgb')
        stroop.setText(thisBlock_7["word"])
        response.keys = []
        response.rt = []
        _response_allKeys = []
        # keep track of which components have finished
        trialComponents = [stroop, response]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1

        # -------Run Routine "trial"-------
        while continueRoutine:
            # get current time
            t = trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame

            # *stroop* updates
            if stroop.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                stroop.frameNStart = frameN  # exact frame index
                stroop.tStart = t  # local t and not account for scr refresh
                stroop.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stroop, 'tStartRefresh')  # time at next scr refresh
                stroop.setAutoDraw(True)
            if stroop.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > stroop.tStartRefresh + 10-frameTolerance:
                    # keep track of stop time/frame for later
                    stroop.tStop = t  # not accounting for scr refresh
                    stroop.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(stroop, 'tStopRefresh')  # time at next scr refresh
                    stroop.setAutoDraw(False)

            # *response* updates
            waitOnFlip = False
            if response.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                response.frameNStart = frameN  # exact frame index
                response.tStart = t  # local t and not account for scr refresh
                response.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(response, 'tStartRefresh')  # time at next scr refresh
                response.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(response.clock.reset)  # t=0 on next screen flip
            if response.status == STARTED and not waitOnFlip:
                theseKeys = response.getKeys(keyList=['r', 'g', 'b', 'y'], waitRelease=False)
                _response_allKeys.extend(theseKeys)
                if len(_response_allKeys):
                    response.keys = _response_allKeys[-1].name  # just the last key pressed
                    response.rt = _response_allKeys[-1].rt
                    # was this correct?
                    if (response.keys == str(thisBlock_7["corrAns"])) or (response.keys == thisBlock_7["corrAns"]):
                        response.corr = 1
                    else:
                        response.corr = 0
                    # a response ends the routine
                    continueRoutine = False

            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()

            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished

            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        block_7.addData('stroop.started', stroop.tStartRefresh)
        block_7.addData('stroop.stopped', stroop.tStopRefresh)
        # check responses
        if response.keys in ['', [], None]:  # No response was made
            response.keys = None
            # was no response the correct answer?!
            if str(corrAns).lower() == 'none':
               response.corr = 1;  # correct non-response
            else:
               response.corr = 0;  # failed to respond (incorrectly)
        # store data for block_7 (TrialHandler)
        block_7.addData('response.keys',response.keys)
        block_7.addData('response.corr', response.corr)
        if response.keys != None:  # we had a response
            block_7.addData('response.rt', response.rt)
        block_7.addData('response.started', response.tStartRefresh)
        block_7.addData('response.stopped', response.tStopRefresh)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()

    # completed 1 repeats of 'block_7'


    # ------Prepare to start Routine "break_2"-------
    continueRoutine = True
    routineTimer.add(60.000000)
    # update component parameters for each repeat
    end_break.keys = []
    end_break.rt = []
    _end_break_allKeys = []
    # keep track of which components have finished
    break_2Components = [break_instructions, end_break]
    for thisComponent in break_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    break_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "break_2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = break_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=break_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *break_instructions* updates
        if break_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            break_instructions.frameNStart = frameN  # exact frame index
            break_instructions.tStart = t  # local t and not account for scr refresh
            break_instructions.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(break_instructions, 'tStartRefresh')  # time at next scr refresh
            break_instructions.setAutoDraw(True)
        if break_instructions.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > break_instructions.tStartRefresh + 60-frameTolerance:
                # keep track of stop time/frame for later
                break_instructions.tStop = t  # not accounting for scr refresh
                break_instructions.frameNStop = frameN  # exact frame index
                win.timeOnFlip(break_instructions, 'tStopRefresh')  # time at next scr refresh
                break_instructions.setAutoDraw(False)

        # *end_break* updates
        waitOnFlip = False
        if end_break.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            end_break.frameNStart = frameN  # exact frame index
            end_break.tStart = t  # local t and not account for scr refresh
            end_break.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(end_break, 'tStartRefresh')  # time at next scr refresh
            end_break.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(end_break.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(end_break.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if end_break.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > end_break.tStartRefresh + 60-frameTolerance:
                # keep track of stop time/frame for later
                end_break.tStop = t  # not accounting for scr refresh
                end_break.frameNStop = frameN  # exact frame index
                win.timeOnFlip(end_break, 'tStopRefresh')  # time at next scr refresh
                end_break.status = FINISHED
        if end_break.status == STARTED and not waitOnFlip:
            theseKeys = end_break.getKeys(keyList=None, waitRelease=False)
            _end_break_allKeys.extend(theseKeys)
            if len(_end_break_allKeys):
                end_break.keys = _end_break_allKeys[-1].name  # just the last key pressed
                end_break.rt = _end_break_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in break_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "break_2"-------
    for thisComponent in break_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('break_instructions.started', break_instructions.tStartRefresh)
    thisExp.addData('break_instructions.stopped', break_instructions.tStopRefresh)

    # set up handler to look after randomisation of conditions etc
    block_8 = data.TrialHandler(nReps=1, method='random',
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('conditionsStroop2.xlsx'),
        seed=None, name='block_8')
    thisExp.addLoop(block_8)  # add the loop to the experiment
    thisBlock_8 = block_8.trialList[0]  # so we can initialise stimuli with some values

    for thisBlock_8 in block_8:
        currentLoop = block_8

        # ------Prepare to start Routine "trial"-------
        continueRoutine = True
        # update component parameters for each repeat
        stroop.setColor(thisBlock_8["colour"], colorSpace='rgb')
        stroop.setText(thisBlock_8["word"])
        response.keys = []
        response.rt = []
        _response_allKeys = []
        # keep track of which components have finished
        trialComponents = [stroop, response]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1

        # -------Run Routine "trial"-------
        while continueRoutine:
            # get current time
            t = trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame

            # *stroop* updates
            if stroop.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                stroop.frameNStart = frameN  # exact frame index
                stroop.tStart = t  # local t and not account for scr refresh
                stroop.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stroop, 'tStartRefresh')  # time at next scr refresh
                stroop.setAutoDraw(True)
            if stroop.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > stroop.tStartRefresh + 10-frameTolerance:
                    # keep track of stop time/frame for later
                    stroop.tStop = t  # not accounting for scr refresh
                    stroop.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(stroop, 'tStopRefresh')  # time at next scr refresh
                    stroop.setAutoDraw(False)

            # *response* updates
            waitOnFlip = False
            if response.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                response.frameNStart = frameN  # exact frame index
                response.tStart = t  # local t and not account for scr refresh
                response.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(response, 'tStartRefresh')  # time at next scr refresh
                response.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(response.clock.reset)  # t=0 on next screen flip
            if response.status == STARTED and not waitOnFlip:
                theseKeys = response.getKeys(keyList=['r', 'g', 'b', 'y'], waitRelease=False)
                _response_allKeys.extend(theseKeys)
                if len(_response_allKeys):
                    response.keys = _response_allKeys[-1].name  # just the last key pressed
                    response.rt = _response_allKeys[-1].rt
                    # was this correct?
                    if (response.keys == str(thisBlock_8["corrAns"])) or (response.keys == thisBlock_8["corrAns"]):
                        response.corr = 1
                    else:
                        response.corr = 0
                    # a response ends the routine
                    continueRoutine = False

            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()

            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished

            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        block_8.addData('stroop.started', stroop.tStartRefresh)
        block_8.addData('stroop.stopped', stroop.tStopRefresh)
        # check responses
        if response.keys in ['', [], None]:  # No response was made
            response.keys = None
            # was no response the correct answer?!
            if str(corrAns).lower() == 'none':
               response.corr = 1;  # correct non-response
            else:
               response.corr = 0;  # failed to respond (incorrectly)
        # store data for block_8 (TrialHandler)
        block_8.addData('response.keys',response.keys)
        block_8.addData('response.corr', response.corr)
        if response.keys != None:  # we had a response
            block_8.addData('response.rt', response.rt)
        block_8.addData('response.started', response.tStartRefresh)
        block_8.addData('response.stopped', response.tStopRefresh)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()

    # completed 1 repeats of 'block_8'


    # ------Prepare to start Routine "break_2"-------
    continueRoutine = True
    routineTimer.add(60.000000)
    # update component parameters for each repeat
    end_break.keys = []
    end_break.rt = []
    _end_break_allKeys = []
    # keep track of which components have finished
    break_2Components = [break_instructions, end_break]
    for thisComponent in break_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    break_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "break_2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = break_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=break_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *break_instructions* updates
        if break_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            break_instructions.frameNStart = frameN  # exact frame index
            break_instructions.tStart = t  # local t and not account for scr refresh
            break_instructions.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(break_instructions, 'tStartRefresh')  # time at next scr refresh
            break_instructions.setAutoDraw(True)
        if break_instructions.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > break_instructions.tStartRefresh + 60-frameTolerance:
                # keep track of stop time/frame for later
                break_instructions.tStop = t  # not accounting for scr refresh
                break_instructions.frameNStop = frameN  # exact frame index
                win.timeOnFlip(break_instructions, 'tStopRefresh')  # time at next scr refresh
                break_instructions.setAutoDraw(False)

        # *end_break* updates
        waitOnFlip = False
        if end_break.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            end_break.frameNStart = frameN  # exact frame index
            end_break.tStart = t  # local t and not account for scr refresh
            end_break.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(end_break, 'tStartRefresh')  # time at next scr refresh
            end_break.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(end_break.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(end_break.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if end_break.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > end_break.tStartRefresh + 60-frameTolerance:
                # keep track of stop time/frame for later
                end_break.tStop = t  # not accounting for scr refresh
                end_break.frameNStop = frameN  # exact frame index
                win.timeOnFlip(end_break, 'tStopRefresh')  # time at next scr refresh
                end_break.status = FINISHED
        if end_break.status == STARTED and not waitOnFlip:
            theseKeys = end_break.getKeys(keyList=None, waitRelease=False)
            _end_break_allKeys.extend(theseKeys)
            if len(_end_break_allKeys):
                end_break.keys = _end_break_allKeys[-1].name  # just the last key pressed
                end_break.rt = _end_break_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in break_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "break_2"-------
    for thisComponent in break_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('break_instructions.started', break_instructions.tStartRefresh)
    thisExp.addData('break_instructions.stopped', break_instructions.tStopRefresh)

    # set up handler to look after randomisation of conditions etc
    block_9 = data.TrialHandler(nReps=1, method='random',
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('conditionsStroop.xlsx'),
        seed=None, name='block_9')
    thisExp.addLoop(block_9)  # add the loop to the experiment
    thisBlock_9 = block_9.trialList[0]  # so we can initialise stimuli with some values

    for thisBlock_9 in block_9:
        currentLoop = block_9

        # ------Prepare to start Routine "trial"-------
        continueRoutine = True
        # update component parameters for each repeat
        stroop.setColor(thisBlock_9["colour"], colorSpace='rgb')
        stroop.setText(thisBlock_9["word"])
        response.keys = []
        response.rt = []
        _response_allKeys = []
        # keep track of which components have finished
        trialComponents = [stroop, response]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1

        # -------Run Routine "trial"-------
        while continueRoutine:
            # get current time
            t = trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame

            # *stroop* updates
            if stroop.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                stroop.frameNStart = frameN  # exact frame index
                stroop.tStart = t  # local t and not account for scr refresh
                stroop.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stroop, 'tStartRefresh')  # time at next scr refresh
                stroop.setAutoDraw(True)
            if stroop.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > stroop.tStartRefresh + 10-frameTolerance:
                    # keep track of stop time/frame for later
                    stroop.tStop = t  # not accounting for scr refresh
                    stroop.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(stroop, 'tStopRefresh')  # time at next scr refresh
                    stroop.setAutoDraw(False)

            # *response* updates
            waitOnFlip = False
            if response.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                response.frameNStart = frameN  # exact frame index
                response.tStart = t  # local t and not account for scr refresh
                response.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(response, 'tStartRefresh')  # time at next scr refresh
                response.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(response.clock.reset)  # t=0 on next screen flip
            if response.status == STARTED and not waitOnFlip:
                theseKeys = response.getKeys(keyList=['r', 'g', 'b', 'y'], waitRelease=False)
                _response_allKeys.extend(theseKeys)
                if len(_response_allKeys):
                    response.keys = _response_allKeys[-1].name  # just the last key pressed
                    response.rt = _response_allKeys[-1].rt
                    # was this correct?
                    if (response.keys == str(thisBlock_9["corrAns"])) or (response.keys == thisBlock_9["corrAns"]):
                        response.corr = 1
                    else:
                        response.corr = 0
                    # a response ends the routine
                    continueRoutine = False

            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()

            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished

            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        block_9.addData('stroop.started', stroop.tStartRefresh)
        block_9.addData('stroop.stopped', stroop.tStopRefresh)
        # check responses
        if response.keys in ['', [], None]:  # No response was made
            response.keys = None
            # was no response the correct answer?!
            if str(corrAns).lower() == 'none':
               response.corr = 1;  # correct non-response
            else:
               response.corr = 0;  # failed to respond (incorrectly)
        # store data for block_9 (TrialHandler)
        block_9.addData('response.keys',response.keys)
        block_9.addData('response.corr', response.corr)
        if response.keys != None:  # we had a response
            block_9.addData('response.rt', response.rt)
        block_9.addData('response.started', response.tStartRefresh)
        block_9.addData('response.stopped', response.tStopRefresh)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()

    # completed 1 repeats of 'block_9'


    # ------Prepare to start Routine "feedback"-------
    continueRoutine = True
    # update component parameters for each repeat
    end_experiment.keys = []
    end_experiment.rt = []
    _end_experiment_allKeys = []
    # keep track of which components have finished
    feedbackComponents = [end_text, end_experiment]
    for thisComponent in feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "feedback"-------
    while continueRoutine:
        # get current time
        t = feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *end_text* updates
        if end_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            end_text.frameNStart = frameN  # exact frame index
            end_text.tStart = t  # local t and not account for scr refresh
            end_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(end_text, 'tStartRefresh')  # time at next scr refresh
            end_text.setAutoDraw(True)

        # *end_experiment* updates
        waitOnFlip = False
        if end_experiment.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            end_experiment.frameNStart = frameN  # exact frame index
            end_experiment.tStart = t  # local t and not account for scr refresh
            end_experiment.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(end_experiment, 'tStartRefresh')  # time at next scr refresh
            end_experiment.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(end_experiment.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(end_experiment.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if end_experiment.status == STARTED and not waitOnFlip:
            theseKeys = end_experiment.getKeys(keyList=None, waitRelease=False)
            _end_experiment_allKeys.extend(theseKeys)
            if len(_end_experiment_allKeys):
                end_experiment.keys = _end_experiment_allKeys[-1].name  # just the last key pressed
                end_experiment.rt = _end_experiment_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('end_text.started', end_text.tStartRefresh)
    thisExp.addData('end_text.stopped', end_text.tStopRefresh)
    # the Routine "feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    # Flip one final time so any remaining win.callOnFlip()
    # and win.timeOnFlip() tasks get executed before quitting
    win.flip()

    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename+'.csv')
    thisExp.saveAsPickle(filename)
    # make sure everything is closed down
    thisExp.abort()  # or data files will save again on exit
    win.close()
    core.quit()


if __name__ == "__main__":
    stroop_stimuli()
