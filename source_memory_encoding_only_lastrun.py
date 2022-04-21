#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.3),
    on April 21, 2022, at 16:20
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.1.3'
expName = 'source_memory_encoding_only'  # from the Builder filename that created this script
expInfo = {'participant': '', 'time': '', 'group': '', 'run': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s_run%s_%s' %(expInfo['participant'], expInfo['time'], expName, expInfo['run'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\stevenweisberg\\Dropbox (UFL)\\Miscellaneous\\SourceMemory\\Source Memory Task T1 & T2\\source_memory_encoding_only_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# Setup ioHub
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# Initialize components for Routine "fixationCross"
fixationCrossClock = core.Clock()
fixation_cross = visual.TextStim(win=win, name='fixation_cross',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
fixation_cross_press_space = keyboard.Keyboard()

# Initialize components for Routine "start1"
start1Clock = core.Clock()
button_check_1 = visual.TextStim(win=win, name='button_check_1',
    text='Press 1',
    font='Arial',
    pos=[0, 0], height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
button_check_resp_1 = keyboard.Keyboard()
import random

encoding_intertrials = [1,1,1,1,1,1,2,2,2,2,2,2,2,2,3,3,3,3,3,3]

retrieval_intertrials = [1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3]

# Initialize components for Routine "start2"
start2Clock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Press 2',
    font='Arial',
    pos=[0, 0], height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "start3"
start3Clock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='Press 3',
    font='Arial',
    pos=[0, 0], height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()

# Initialize components for Routine "start4"
start4Clock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='Press 4',
    font='Arial',
    pos=[0, 0], height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "scan_ready"
scan_readyClock = core.Clock()
wait_text = visual.TextStim(win=win, name='wait_text',
    text='The experiment will begin shortly',
    font='Arial',
    pos=[0, 0], height=0.15, wrapWidth=2, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
scanner_pulse = keyboard.Keyboard()

# Initialize components for Routine "encodeFMRI"
encodeFMRIClock = core.Clock()
instruction = visual.TextStim(win=win, name='instruction',
    text='Imagine',
    font='Arial',
    pos=[0, 0.6], height=0.15, wrapWidth=2, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
image_3 = visual.ImageStim(
    win=win,
    name='image_3', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=[0, 0], size=[0.6, 0.6],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
in_ = visual.TextStim(win=win, name='in_',
    text='in',
    font='Arial',
    pos=[0, -0.5], height=0.15, wrapWidth=2, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
source_cue = visual.TextStim(win=win, name='source_cue',
    text='',
    font='Arial',
    pos=[0, -0.7], height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
fixation = visual.TextStim(win=win, name='fixation',
    text='+',
    font='Arial',
    pos=[0, 0], height=0.3, wrapWidth=2, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);

# Initialize components for Routine "rateFMRI"
rateFMRIClock = core.Clock()
rating = visual.TextStim(win=win, name='rating',
    text='    How well did you do?\n\n\n\n1           2          3            4',
    font='Arial',
    pos=[0, 0.2], height=0.15, wrapWidth=2, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text = visual.TextStim(win=win, name='text',
    text='   (unable)                                                         (very clearly)',
    font='Arial',
    pos=[0, -0.35], height=0.08, wrapWidth=2, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
rating_resp = keyboard.Keyboard()

# Initialize components for Routine "ITI"
ITIClock = core.Clock()
text_16 = visual.TextStim(win=win, name='text_16',
    text='+',
    font='Arial',
    pos=[0, 0], height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "encodeFMRI"
encodeFMRIClock = core.Clock()
instruction = visual.TextStim(win=win, name='instruction',
    text='Imagine',
    font='Arial',
    pos=[0, 0.6], height=0.15, wrapWidth=2, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
image_3 = visual.ImageStim(
    win=win,
    name='image_3', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=[0, 0], size=[0.6, 0.6],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
in_ = visual.TextStim(win=win, name='in_',
    text='in',
    font='Arial',
    pos=[0, -0.5], height=0.15, wrapWidth=2, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
source_cue = visual.TextStim(win=win, name='source_cue',
    text='',
    font='Arial',
    pos=[0, -0.7], height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
fixation = visual.TextStim(win=win, name='fixation',
    text='+',
    font='Arial',
    pos=[0, 0], height=0.3, wrapWidth=2, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);

# Initialize components for Routine "rateFMRI"
rateFMRIClock = core.Clock()
rating = visual.TextStim(win=win, name='rating',
    text='    How well did you do?\n\n\n\n1           2          3            4',
    font='Arial',
    pos=[0, 0.2], height=0.15, wrapWidth=2, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text = visual.TextStim(win=win, name='text',
    text='   (unable)                                                         (very clearly)',
    font='Arial',
    pos=[0, -0.35], height=0.08, wrapWidth=2, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
rating_resp = keyboard.Keyboard()

# Initialize components for Routine "ITI"
ITIClock = core.Clock()
text_16 = visual.TextStim(win=win, name='text_16',
    text='+',
    font='Arial',
    pos=[0, 0], height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "distractInstruct"
distractInstructClock = core.Clock()
instruc = visual.TextStim(win=win, name='instruc',
    text='Press 1 for X\nPress 2 for O',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "distractorFMRI"
distractorFMRIClock = core.Clock()
distractor_task = visual.TextStim(win=win, name='distractor_task',
    text='',
    font='Arial',
    pos=[0, 0], height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
distractor_task_resp = keyboard.Keyboard()
flicker = visual.TextStim(win=win, name='flicker',
    text=' ',
    font='Arial',
    pos=[0, 0], height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "pauseFMRI"
pauseFMRIClock = core.Clock()
end_screen = visual.TextStim(win=win, name='end_screen',
    text='End of this scan',
    font='Arial',
    pos=[0, 0], height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "fixationCross"-------
continueRoutine = True
# update component parameters for each repeat
fixation_cross_press_space.keys = []
fixation_cross_press_space.rt = []
_fixation_cross_press_space_allKeys = []
# keep track of which components have finished
fixationCrossComponents = [fixation_cross, fixation_cross_press_space]
for thisComponent in fixationCrossComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
fixationCrossClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "fixationCross"-------
while continueRoutine:
    # get current time
    t = fixationCrossClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=fixationCrossClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fixation_cross* updates
    if fixation_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fixation_cross.frameNStart = frameN  # exact frame index
        fixation_cross.tStart = t  # local t and not account for scr refresh
        fixation_cross.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fixation_cross, 'tStartRefresh')  # time at next scr refresh
        fixation_cross.setAutoDraw(True)
    
    # *fixation_cross_press_space* updates
    waitOnFlip = False
    if fixation_cross_press_space.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fixation_cross_press_space.frameNStart = frameN  # exact frame index
        fixation_cross_press_space.tStart = t  # local t and not account for scr refresh
        fixation_cross_press_space.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fixation_cross_press_space, 'tStartRefresh')  # time at next scr refresh
        fixation_cross_press_space.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(fixation_cross_press_space.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(fixation_cross_press_space.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if fixation_cross_press_space.status == STARTED and not waitOnFlip:
        theseKeys = fixation_cross_press_space.getKeys(keyList=['space'], waitRelease=False)
        _fixation_cross_press_space_allKeys.extend(theseKeys)
        if len(_fixation_cross_press_space_allKeys):
            fixation_cross_press_space.keys = _fixation_cross_press_space_allKeys[-1].name  # just the last key pressed
            fixation_cross_press_space.rt = _fixation_cross_press_space_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fixationCrossComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "fixationCross"-------
for thisComponent in fixationCrossComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('fixation_cross.started', fixation_cross.tStartRefresh)
thisExp.addData('fixation_cross.stopped', fixation_cross.tStopRefresh)
# check responses
if fixation_cross_press_space.keys in ['', [], None]:  # No response was made
    fixation_cross_press_space.keys = None
thisExp.addData('fixation_cross_press_space.keys',fixation_cross_press_space.keys)
if fixation_cross_press_space.keys != None:  # we had a response
    thisExp.addData('fixation_cross_press_space.rt', fixation_cross_press_space.rt)
thisExp.addData('fixation_cross_press_space.started', fixation_cross_press_space.tStartRefresh)
thisExp.addData('fixation_cross_press_space.stopped', fixation_cross_press_space.tStopRefresh)
thisExp.nextEntry()
# the Routine "fixationCross" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "start1"-------
continueRoutine = True
# update component parameters for each repeat
button_check_resp_1.keys = []
button_check_resp_1.rt = []
_button_check_resp_1_allKeys = []
# keep track of which components have finished
start1Components = [button_check_1, button_check_resp_1]
for thisComponent in start1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
start1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "start1"-------
while continueRoutine:
    # get current time
    t = start1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=start1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *button_check_1* updates
    if button_check_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        button_check_1.frameNStart = frameN  # exact frame index
        button_check_1.tStart = t  # local t and not account for scr refresh
        button_check_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button_check_1, 'tStartRefresh')  # time at next scr refresh
        button_check_1.setAutoDraw(True)
    
    # *button_check_resp_1* updates
    waitOnFlip = False
    if button_check_resp_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        button_check_resp_1.frameNStart = frameN  # exact frame index
        button_check_resp_1.tStart = t  # local t and not account for scr refresh
        button_check_resp_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button_check_resp_1, 'tStartRefresh')  # time at next scr refresh
        button_check_resp_1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(button_check_resp_1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(button_check_resp_1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if button_check_resp_1.status == STARTED and not waitOnFlip:
        theseKeys = button_check_resp_1.getKeys(keyList=['1'], waitRelease=False)
        _button_check_resp_1_allKeys.extend(theseKeys)
        if len(_button_check_resp_1_allKeys):
            button_check_resp_1.keys = _button_check_resp_1_allKeys[-1].name  # just the last key pressed
            button_check_resp_1.rt = _button_check_resp_1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in start1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "start1"-------
for thisComponent in start1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('button_check_1.started', button_check_1.tStartRefresh)
thisExp.addData('button_check_1.stopped', button_check_1.tStopRefresh)
# check responses
if button_check_resp_1.keys in ['', [], None]:  # No response was made
    button_check_resp_1.keys = None
thisExp.addData('button_check_resp_1.keys',button_check_resp_1.keys)
if button_check_resp_1.keys != None:  # we had a response
    thisExp.addData('button_check_resp_1.rt', button_check_resp_1.rt)
thisExp.addData('button_check_resp_1.started', button_check_resp_1.tStartRefresh)
thisExp.addData('button_check_resp_1.stopped', button_check_resp_1.tStopRefresh)
thisExp.nextEntry()
# the Routine "start1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "start2"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
start2Components = [text_2, key_resp_3]
for thisComponent in start2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
start2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "start2"-------
while continueRoutine:
    # get current time
    t = start2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=start2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['2'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in start2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "start2"-------
for thisComponent in start2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.addData('key_resp_3.started', key_resp_3.tStartRefresh)
thisExp.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
thisExp.nextEntry()
# the Routine "start2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "start3"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_4.keys = []
key_resp_4.rt = []
_key_resp_4_allKeys = []
# keep track of which components have finished
start3Components = [text_3, key_resp_4]
for thisComponent in start3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
start3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "start3"-------
while continueRoutine:
    # get current time
    t = start3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=start3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        text_3.setAutoDraw(True)
    
    # *key_resp_4* updates
    waitOnFlip = False
    if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.tStart = t  # local t and not account for scr refresh
        key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_4.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_4.getKeys(keyList=['3'], waitRelease=False)
        _key_resp_4_allKeys.extend(theseKeys)
        if len(_key_resp_4_allKeys):
            key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
            key_resp_4.rt = _key_resp_4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in start3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "start3"-------
for thisComponent in start3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_3.started', text_3.tStartRefresh)
thisExp.addData('text_3.stopped', text_3.tStopRefresh)
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
    key_resp_4.keys = None
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.addData('key_resp_4.started', key_resp_4.tStartRefresh)
thisExp.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
thisExp.nextEntry()
# the Routine "start3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "start4"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
# keep track of which components have finished
start4Components = [text_4, key_resp_5]
for thisComponent in start4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
start4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "start4"-------
while continueRoutine:
    # get current time
    t = start4Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=start4Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_4* updates
    if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_4.frameNStart = frameN  # exact frame index
        text_4.tStart = t  # local t and not account for scr refresh
        text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
        text_4.setAutoDraw(True)
    
    # *key_resp_5* updates
    waitOnFlip = False
    if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.tStart = t  # local t and not account for scr refresh
        key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_5.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_5.getKeys(keyList=['4'], waitRelease=False)
        _key_resp_5_allKeys.extend(theseKeys)
        if len(_key_resp_5_allKeys):
            key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
            key_resp_5.rt = _key_resp_5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in start4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "start4"-------
for thisComponent in start4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_4.started', text_4.tStartRefresh)
thisExp.addData('text_4.stopped', text_4.tStopRefresh)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
    key_resp_5.keys = None
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.addData('key_resp_5.started', key_resp_5.tStartRefresh)
thisExp.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
thisExp.nextEntry()
# the Routine "start4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "scan_ready"-------
continueRoutine = True
# update component parameters for each repeat
scanner_pulse.keys = []
scanner_pulse.rt = []
_scanner_pulse_allKeys = []
timerStarted = False
totalTrials = 0
random.shuffle(encoding_intertrials)
random.shuffle(retrieval_intertrials)
# keep track of which components have finished
scan_readyComponents = [wait_text, scanner_pulse]
for thisComponent in scan_readyComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
scan_readyClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "scan_ready"-------
while continueRoutine:
    # get current time
    t = scan_readyClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=scan_readyClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *wait_text* updates
    if wait_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        wait_text.frameNStart = frameN  # exact frame index
        wait_text.tStart = t  # local t and not account for scr refresh
        wait_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(wait_text, 'tStartRefresh')  # time at next scr refresh
        wait_text.setAutoDraw(True)
    
    # *scanner_pulse* updates
    waitOnFlip = False
    if scanner_pulse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        scanner_pulse.frameNStart = frameN  # exact frame index
        scanner_pulse.tStart = t  # local t and not account for scr refresh
        scanner_pulse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(scanner_pulse, 'tStartRefresh')  # time at next scr refresh
        scanner_pulse.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(scanner_pulse.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(scanner_pulse.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if scanner_pulse.status == STARTED and not waitOnFlip:
        theseKeys = scanner_pulse.getKeys(keyList=['5','t','T'], waitRelease=False)
        _scanner_pulse_allKeys.extend(theseKeys)
        if len(_scanner_pulse_allKeys):
            scanner_pulse.keys = _scanner_pulse_allKeys[-1].name  # just the last key pressed
            scanner_pulse.rt = _scanner_pulse_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in scan_readyComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "scan_ready"-------
for thisComponent in scan_readyComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('wait_text.started', wait_text.tStartRefresh)
thisExp.addData('wait_text.stopped', wait_text.tStopRefresh)
# check responses
if scanner_pulse.keys in ['', [], None]:  # No response was made
    scanner_pulse.keys = None
thisExp.addData('scanner_pulse.keys',scanner_pulse.keys)
if scanner_pulse.keys != None:  # we had a response
    thisExp.addData('scanner_pulse.rt', scanner_pulse.rt)
thisExp.addData('scanner_pulse.started', scanner_pulse.tStartRefresh)
thisExp.addData('scanner_pulse.stopped', scanner_pulse.tStopRefresh)
thisExp.nextEntry()
# the Routine "scan_ready" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
encode_trials1 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('condition_files/encoding_g'+expInfo['group']+'_b' + expInfo['run'] + '.xlsx', selection='0:10'),
    seed=None, name='encode_trials1')
thisExp.addLoop(encode_trials1)  # add the loop to the experiment
thisEncode_trials1 = encode_trials1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisEncode_trials1.rgb)
if thisEncode_trials1 != None:
    for paramName in thisEncode_trials1:
        exec('{} = thisEncode_trials1[paramName]'.format(paramName))

for thisEncode_trials1 in encode_trials1:
    currentLoop = encode_trials1
    # abbreviate parameter names if possible (e.g. rgb = thisEncode_trials1.rgb)
    if thisEncode_trials1 != None:
        for paramName in thisEncode_trials1:
            exec('{} = thisEncode_trials1[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "encodeFMRI"-------
    continueRoutine = True
    routineTimer.add(6.000000)
    # update component parameters for each repeat
    if not timerStarted:
        scanStartTime = globalClock.getTime()
        timerStarted = True
    
    thisExp.addData("Trial_cue_onset", globalClock.getTime() - scanStartTime)
    image_3.setImage('stimulus_images_' + expInfo['time'] + '/' + stimImg)
    source_cue.setText(taskType)
    # keep track of which components have finished
    encodeFMRIComponents = [instruction, image_3, in_, source_cue, fixation]
    for thisComponent in encodeFMRIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    encodeFMRIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "encodeFMRI"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = encodeFMRIClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=encodeFMRIClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instruction* updates
        if instruction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instruction.frameNStart = frameN  # exact frame index
            instruction.tStart = t  # local t and not account for scr refresh
            instruction.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruction, 'tStartRefresh')  # time at next scr refresh
            instruction.setAutoDraw(True)
        if instruction.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > instruction.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                instruction.tStop = t  # not accounting for scr refresh
                instruction.frameNStop = frameN  # exact frame index
                win.timeOnFlip(instruction, 'tStopRefresh')  # time at next scr refresh
                instruction.setAutoDraw(False)
        
        # *image_3* updates
        if image_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_3.frameNStart = frameN  # exact frame index
            image_3.tStart = t  # local t and not account for scr refresh
            image_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
            image_3.setAutoDraw(True)
        if image_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_3.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                image_3.tStop = t  # not accounting for scr refresh
                image_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_3, 'tStopRefresh')  # time at next scr refresh
                image_3.setAutoDraw(False)
        
        # *in_* updates
        if in_.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            in_.frameNStart = frameN  # exact frame index
            in_.tStart = t  # local t and not account for scr refresh
            in_.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(in_, 'tStartRefresh')  # time at next scr refresh
            in_.setAutoDraw(True)
        if in_.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > in_.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                in_.tStop = t  # not accounting for scr refresh
                in_.frameNStop = frameN  # exact frame index
                win.timeOnFlip(in_, 'tStopRefresh')  # time at next scr refresh
                in_.setAutoDraw(False)
        
        # *source_cue* updates
        if source_cue.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            source_cue.frameNStart = frameN  # exact frame index
            source_cue.tStart = t  # local t and not account for scr refresh
            source_cue.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(source_cue, 'tStartRefresh')  # time at next scr refresh
            source_cue.setAutoDraw(True)
        if source_cue.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > source_cue.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                source_cue.tStop = t  # not accounting for scr refresh
                source_cue.frameNStop = frameN  # exact frame index
                win.timeOnFlip(source_cue, 'tStopRefresh')  # time at next scr refresh
                source_cue.setAutoDraw(False)
        
        # *fixation* updates
        if fixation.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            fixation.frameNStart = frameN  # exact frame index
            fixation.tStart = t  # local t and not account for scr refresh
            fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
            fixation.setAutoDraw(True)
        if fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation.tStartRefresh + 4.0-frameTolerance:
                # keep track of stop time/frame for later
                fixation.tStop = t  # not accounting for scr refresh
                fixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation, 'tStopRefresh')  # time at next scr refresh
                fixation.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in encodeFMRIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "encodeFMRI"-------
    for thisComponent in encodeFMRIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    encode_trials1.addData('instruction.started', instruction.tStartRefresh)
    encode_trials1.addData('instruction.stopped', instruction.tStopRefresh)
    encode_trials1.addData('image_3.started', image_3.tStartRefresh)
    encode_trials1.addData('image_3.stopped', image_3.tStopRefresh)
    encode_trials1.addData('in_.started', in_.tStartRefresh)
    encode_trials1.addData('in_.stopped', in_.tStopRefresh)
    encode_trials1.addData('source_cue.started', source_cue.tStartRefresh)
    encode_trials1.addData('source_cue.stopped', source_cue.tStopRefresh)
    encode_trials1.addData('fixation.started', fixation.tStartRefresh)
    encode_trials1.addData('fixation.stopped', fixation.tStopRefresh)
    
    # ------Prepare to start Routine "rateFMRI"-------
    continueRoutine = True
    routineTimer.add(6.000000)
    # update component parameters for each repeat
    type_encoding = 1
    type_retrieval = 0
    thisExp.addData("Response_cue_onset", globalClock.getTime() - scanStartTime)
    rating_resp.keys = []
    rating_resp.rt = []
    _rating_resp_allKeys = []
    # keep track of which components have finished
    rateFMRIComponents = [rating, text, rating_resp]
    for thisComponent in rateFMRIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    rateFMRIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "rateFMRI"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = rateFMRIClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=rateFMRIClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *rating* updates
        if rating.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rating.frameNStart = frameN  # exact frame index
            rating.tStart = t  # local t and not account for scr refresh
            rating.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rating, 'tStartRefresh')  # time at next scr refresh
            rating.setAutoDraw(True)
        if rating.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rating.tStartRefresh + 6.0-frameTolerance:
                # keep track of stop time/frame for later
                rating.tStop = t  # not accounting for scr refresh
                rating.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rating, 'tStopRefresh')  # time at next scr refresh
                rating.setAutoDraw(False)
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 6.0-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                text.setAutoDraw(False)
        
        # *rating_resp* updates
        waitOnFlip = False
        if rating_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rating_resp.frameNStart = frameN  # exact frame index
            rating_resp.tStart = t  # local t and not account for scr refresh
            rating_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rating_resp, 'tStartRefresh')  # time at next scr refresh
            rating_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(rating_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(rating_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if rating_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rating_resp.tStartRefresh + 6.0-frameTolerance:
                # keep track of stop time/frame for later
                rating_resp.tStop = t  # not accounting for scr refresh
                rating_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rating_resp, 'tStopRefresh')  # time at next scr refresh
                rating_resp.status = FINISHED
        if rating_resp.status == STARTED and not waitOnFlip:
            theseKeys = rating_resp.getKeys(keyList=['1','2','3','4'], waitRelease=False)
            _rating_resp_allKeys.extend(theseKeys)
            if len(_rating_resp_allKeys):
                rating_resp.keys = _rating_resp_allKeys[-1].name  # just the last key pressed
                rating_resp.rt = _rating_resp_allKeys[-1].rt
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in rateFMRIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "rateFMRI"-------
    for thisComponent in rateFMRIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    encode_trials1.addData('rating.started', rating.tStartRefresh)
    encode_trials1.addData('rating.stopped', rating.tStopRefresh)
    encode_trials1.addData('text.started', text.tStartRefresh)
    encode_trials1.addData('text.stopped', text.tStopRefresh)
    # check responses
    if rating_resp.keys in ['', [], None]:  # No response was made
        rating_resp.keys = None
    encode_trials1.addData('rating_resp.keys',rating_resp.keys)
    if rating_resp.keys != None:  # we had a response
        encode_trials1.addData('rating_resp.rt', rating_resp.rt)
    encode_trials1.addData('rating_resp.started', rating_resp.tStartRefresh)
    encode_trials1.addData('rating_resp.stopped', rating_resp.tStopRefresh)
    
    # ------Prepare to start Routine "ITI"-------
    continueRoutine = True
    # update component parameters for each repeat
    if type_encoding == 1:
        ITI_length = encoding_intertrials[totalTrials]
    elif type_retrieval == 1:
        ITI_length = retrieval_intertrials[totalTrials]
    # keep track of which components have finished
    ITIComponents = [text_16]
    for thisComponent in ITIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ITIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "ITI"-------
    while continueRoutine:
        # get current time
        t = ITIClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ITIClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_16* updates
        if text_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_16.frameNStart = frameN  # exact frame index
            text_16.tStart = t  # local t and not account for scr refresh
            text_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_16, 'tStartRefresh')  # time at next scr refresh
            text_16.setAutoDraw(True)
        if text_16.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_16.tStartRefresh + ITI_length-frameTolerance:
                # keep track of stop time/frame for later
                text_16.tStop = t  # not accounting for scr refresh
                text_16.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_16, 'tStopRefresh')  # time at next scr refresh
                text_16.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ITI"-------
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    totalTrials = totalTrials + 1
    encode_trials1.addData('text_16.started', text_16.tStartRefresh)
    encode_trials1.addData('text_16.stopped', text_16.tStopRefresh)
    # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'encode_trials1'


# set up handler to look after randomisation of conditions etc
encode_trials2 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('condition_files/encoding_g'+expInfo['group']+'_b' + expInfo['run'] + '.xlsx', selection='10:20'),
    seed=None, name='encode_trials2')
thisExp.addLoop(encode_trials2)  # add the loop to the experiment
thisEncode_trials2 = encode_trials2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisEncode_trials2.rgb)
if thisEncode_trials2 != None:
    for paramName in thisEncode_trials2:
        exec('{} = thisEncode_trials2[paramName]'.format(paramName))

for thisEncode_trials2 in encode_trials2:
    currentLoop = encode_trials2
    # abbreviate parameter names if possible (e.g. rgb = thisEncode_trials2.rgb)
    if thisEncode_trials2 != None:
        for paramName in thisEncode_trials2:
            exec('{} = thisEncode_trials2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "encodeFMRI"-------
    continueRoutine = True
    routineTimer.add(6.000000)
    # update component parameters for each repeat
    if not timerStarted:
        scanStartTime = globalClock.getTime()
        timerStarted = True
    
    thisExp.addData("Trial_cue_onset", globalClock.getTime() - scanStartTime)
    image_3.setImage('stimulus_images_' + expInfo['time'] + '/' + stimImg)
    source_cue.setText(taskType)
    # keep track of which components have finished
    encodeFMRIComponents = [instruction, image_3, in_, source_cue, fixation]
    for thisComponent in encodeFMRIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    encodeFMRIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "encodeFMRI"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = encodeFMRIClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=encodeFMRIClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instruction* updates
        if instruction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instruction.frameNStart = frameN  # exact frame index
            instruction.tStart = t  # local t and not account for scr refresh
            instruction.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruction, 'tStartRefresh')  # time at next scr refresh
            instruction.setAutoDraw(True)
        if instruction.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > instruction.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                instruction.tStop = t  # not accounting for scr refresh
                instruction.frameNStop = frameN  # exact frame index
                win.timeOnFlip(instruction, 'tStopRefresh')  # time at next scr refresh
                instruction.setAutoDraw(False)
        
        # *image_3* updates
        if image_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_3.frameNStart = frameN  # exact frame index
            image_3.tStart = t  # local t and not account for scr refresh
            image_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
            image_3.setAutoDraw(True)
        if image_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_3.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                image_3.tStop = t  # not accounting for scr refresh
                image_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_3, 'tStopRefresh')  # time at next scr refresh
                image_3.setAutoDraw(False)
        
        # *in_* updates
        if in_.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            in_.frameNStart = frameN  # exact frame index
            in_.tStart = t  # local t and not account for scr refresh
            in_.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(in_, 'tStartRefresh')  # time at next scr refresh
            in_.setAutoDraw(True)
        if in_.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > in_.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                in_.tStop = t  # not accounting for scr refresh
                in_.frameNStop = frameN  # exact frame index
                win.timeOnFlip(in_, 'tStopRefresh')  # time at next scr refresh
                in_.setAutoDraw(False)
        
        # *source_cue* updates
        if source_cue.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            source_cue.frameNStart = frameN  # exact frame index
            source_cue.tStart = t  # local t and not account for scr refresh
            source_cue.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(source_cue, 'tStartRefresh')  # time at next scr refresh
            source_cue.setAutoDraw(True)
        if source_cue.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > source_cue.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                source_cue.tStop = t  # not accounting for scr refresh
                source_cue.frameNStop = frameN  # exact frame index
                win.timeOnFlip(source_cue, 'tStopRefresh')  # time at next scr refresh
                source_cue.setAutoDraw(False)
        
        # *fixation* updates
        if fixation.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            fixation.frameNStart = frameN  # exact frame index
            fixation.tStart = t  # local t and not account for scr refresh
            fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
            fixation.setAutoDraw(True)
        if fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation.tStartRefresh + 4.0-frameTolerance:
                # keep track of stop time/frame for later
                fixation.tStop = t  # not accounting for scr refresh
                fixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation, 'tStopRefresh')  # time at next scr refresh
                fixation.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in encodeFMRIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "encodeFMRI"-------
    for thisComponent in encodeFMRIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    encode_trials2.addData('instruction.started', instruction.tStartRefresh)
    encode_trials2.addData('instruction.stopped', instruction.tStopRefresh)
    encode_trials2.addData('image_3.started', image_3.tStartRefresh)
    encode_trials2.addData('image_3.stopped', image_3.tStopRefresh)
    encode_trials2.addData('in_.started', in_.tStartRefresh)
    encode_trials2.addData('in_.stopped', in_.tStopRefresh)
    encode_trials2.addData('source_cue.started', source_cue.tStartRefresh)
    encode_trials2.addData('source_cue.stopped', source_cue.tStopRefresh)
    encode_trials2.addData('fixation.started', fixation.tStartRefresh)
    encode_trials2.addData('fixation.stopped', fixation.tStopRefresh)
    
    # ------Prepare to start Routine "rateFMRI"-------
    continueRoutine = True
    routineTimer.add(6.000000)
    # update component parameters for each repeat
    type_encoding = 1
    type_retrieval = 0
    thisExp.addData("Response_cue_onset", globalClock.getTime() - scanStartTime)
    rating_resp.keys = []
    rating_resp.rt = []
    _rating_resp_allKeys = []
    # keep track of which components have finished
    rateFMRIComponents = [rating, text, rating_resp]
    for thisComponent in rateFMRIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    rateFMRIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "rateFMRI"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = rateFMRIClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=rateFMRIClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *rating* updates
        if rating.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rating.frameNStart = frameN  # exact frame index
            rating.tStart = t  # local t and not account for scr refresh
            rating.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rating, 'tStartRefresh')  # time at next scr refresh
            rating.setAutoDraw(True)
        if rating.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rating.tStartRefresh + 6.0-frameTolerance:
                # keep track of stop time/frame for later
                rating.tStop = t  # not accounting for scr refresh
                rating.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rating, 'tStopRefresh')  # time at next scr refresh
                rating.setAutoDraw(False)
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 6.0-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                text.setAutoDraw(False)
        
        # *rating_resp* updates
        waitOnFlip = False
        if rating_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rating_resp.frameNStart = frameN  # exact frame index
            rating_resp.tStart = t  # local t and not account for scr refresh
            rating_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rating_resp, 'tStartRefresh')  # time at next scr refresh
            rating_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(rating_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(rating_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if rating_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rating_resp.tStartRefresh + 6.0-frameTolerance:
                # keep track of stop time/frame for later
                rating_resp.tStop = t  # not accounting for scr refresh
                rating_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rating_resp, 'tStopRefresh')  # time at next scr refresh
                rating_resp.status = FINISHED
        if rating_resp.status == STARTED and not waitOnFlip:
            theseKeys = rating_resp.getKeys(keyList=['1','2','3','4'], waitRelease=False)
            _rating_resp_allKeys.extend(theseKeys)
            if len(_rating_resp_allKeys):
                rating_resp.keys = _rating_resp_allKeys[-1].name  # just the last key pressed
                rating_resp.rt = _rating_resp_allKeys[-1].rt
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in rateFMRIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "rateFMRI"-------
    for thisComponent in rateFMRIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    encode_trials2.addData('rating.started', rating.tStartRefresh)
    encode_trials2.addData('rating.stopped', rating.tStopRefresh)
    encode_trials2.addData('text.started', text.tStartRefresh)
    encode_trials2.addData('text.stopped', text.tStopRefresh)
    # check responses
    if rating_resp.keys in ['', [], None]:  # No response was made
        rating_resp.keys = None
    encode_trials2.addData('rating_resp.keys',rating_resp.keys)
    if rating_resp.keys != None:  # we had a response
        encode_trials2.addData('rating_resp.rt', rating_resp.rt)
    encode_trials2.addData('rating_resp.started', rating_resp.tStartRefresh)
    encode_trials2.addData('rating_resp.stopped', rating_resp.tStopRefresh)
    
    # ------Prepare to start Routine "ITI"-------
    continueRoutine = True
    # update component parameters for each repeat
    if type_encoding == 1:
        ITI_length = encoding_intertrials[totalTrials]
    elif type_retrieval == 1:
        ITI_length = retrieval_intertrials[totalTrials]
    # keep track of which components have finished
    ITIComponents = [text_16]
    for thisComponent in ITIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ITIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "ITI"-------
    while continueRoutine:
        # get current time
        t = ITIClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ITIClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_16* updates
        if text_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_16.frameNStart = frameN  # exact frame index
            text_16.tStart = t  # local t and not account for scr refresh
            text_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_16, 'tStartRefresh')  # time at next scr refresh
            text_16.setAutoDraw(True)
        if text_16.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_16.tStartRefresh + ITI_length-frameTolerance:
                # keep track of stop time/frame for later
                text_16.tStop = t  # not accounting for scr refresh
                text_16.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_16, 'tStopRefresh')  # time at next scr refresh
                text_16.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ITI"-------
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    totalTrials = totalTrials + 1
    encode_trials2.addData('text_16.started', text_16.tStartRefresh)
    encode_trials2.addData('text_16.stopped', text_16.tStopRefresh)
    # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'encode_trials2'


# ------Prepare to start Routine "distractInstruct"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
distractInstructComponents = [instruc]
for thisComponent in distractInstructComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
distractInstructClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "distractInstruct"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = distractInstructClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=distractInstructClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruc* updates
    if instruc.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruc.frameNStart = frameN  # exact frame index
        instruc.tStart = t  # local t and not account for scr refresh
        instruc.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruc, 'tStartRefresh')  # time at next scr refresh
        instruc.setAutoDraw(True)
    if instruc.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instruc.tStartRefresh + 3.0-frameTolerance:
            # keep track of stop time/frame for later
            instruc.tStop = t  # not accounting for scr refresh
            instruc.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instruc, 'tStopRefresh')  # time at next scr refresh
            instruc.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in distractInstructComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "distractInstruct"-------
for thisComponent in distractInstructComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instruc.started', instruc.tStartRefresh)
thisExp.addData('instruc.stopped', instruc.tStopRefresh)

# set up handler to look after randomisation of conditions etc
distractor = data.TrialHandler(nReps=30, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('condition_files/distractor.xlsx'),
    seed=None, name='distractor')
thisExp.addLoop(distractor)  # add the loop to the experiment
thisDistractor = distractor.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisDistractor.rgb)
if thisDistractor != None:
    for paramName in thisDistractor:
        exec('{} = thisDistractor[paramName]'.format(paramName))

for thisDistractor in distractor:
    currentLoop = distractor
    # abbreviate parameter names if possible (e.g. rgb = thisDistractor.rgb)
    if thisDistractor != None:
        for paramName in thisDistractor:
            exec('{} = thisDistractor[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "distractorFMRI"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    distractor_task.setText(letter)
    distractor_task_resp.keys = []
    distractor_task_resp.rt = []
    _distractor_task_resp_allKeys = []
    # keep track of which components have finished
    distractorFMRIComponents = [distractor_task, distractor_task_resp, flicker]
    for thisComponent in distractorFMRIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    distractorFMRIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "distractorFMRI"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = distractorFMRIClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=distractorFMRIClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *distractor_task* updates
        if distractor_task.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            distractor_task.frameNStart = frameN  # exact frame index
            distractor_task.tStart = t  # local t and not account for scr refresh
            distractor_task.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(distractor_task, 'tStartRefresh')  # time at next scr refresh
            distractor_task.setAutoDraw(True)
        if distractor_task.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > distractor_task.tStartRefresh + 0.95-frameTolerance:
                # keep track of stop time/frame for later
                distractor_task.tStop = t  # not accounting for scr refresh
                distractor_task.frameNStop = frameN  # exact frame index
                win.timeOnFlip(distractor_task, 'tStopRefresh')  # time at next scr refresh
                distractor_task.setAutoDraw(False)
        
        # *distractor_task_resp* updates
        waitOnFlip = False
        if distractor_task_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            distractor_task_resp.frameNStart = frameN  # exact frame index
            distractor_task_resp.tStart = t  # local t and not account for scr refresh
            distractor_task_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(distractor_task_resp, 'tStartRefresh')  # time at next scr refresh
            distractor_task_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(distractor_task_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(distractor_task_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if distractor_task_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > distractor_task_resp.tStartRefresh + 0.95-frameTolerance:
                # keep track of stop time/frame for later
                distractor_task_resp.tStop = t  # not accounting for scr refresh
                distractor_task_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(distractor_task_resp, 'tStopRefresh')  # time at next scr refresh
                distractor_task_resp.status = FINISHED
        if distractor_task_resp.status == STARTED and not waitOnFlip:
            theseKeys = distractor_task_resp.getKeys(keyList=['1','2'], waitRelease=False)
            _distractor_task_resp_allKeys.extend(theseKeys)
            if len(_distractor_task_resp_allKeys):
                distractor_task_resp.keys = _distractor_task_resp_allKeys[-1].name  # just the last key pressed
                distractor_task_resp.rt = _distractor_task_resp_allKeys[-1].rt
                # was this correct?
                if (distractor_task_resp.keys == str(correctResponse)) or (distractor_task_resp.keys == correctResponse):
                    distractor_task_resp.corr = 1
                else:
                    distractor_task_resp.corr = 0
        
        # *flicker* updates
        if flicker.status == NOT_STARTED and tThisFlip >= 0.95-frameTolerance:
            # keep track of start time/frame for later
            flicker.frameNStart = frameN  # exact frame index
            flicker.tStart = t  # local t and not account for scr refresh
            flicker.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(flicker, 'tStartRefresh')  # time at next scr refresh
            flicker.setAutoDraw(True)
        if flicker.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > flicker.tStartRefresh + 0.05-frameTolerance:
                # keep track of stop time/frame for later
                flicker.tStop = t  # not accounting for scr refresh
                flicker.frameNStop = frameN  # exact frame index
                win.timeOnFlip(flicker, 'tStopRefresh')  # time at next scr refresh
                flicker.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in distractorFMRIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "distractorFMRI"-------
    for thisComponent in distractorFMRIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    distractor.addData('distractor_task.started', distractor_task.tStartRefresh)
    distractor.addData('distractor_task.stopped', distractor_task.tStopRefresh)
    # check responses
    if distractor_task_resp.keys in ['', [], None]:  # No response was made
        distractor_task_resp.keys = None
        # was no response the correct answer?!
        if str(correctResponse).lower() == 'none':
           distractor_task_resp.corr = 1;  # correct non-response
        else:
           distractor_task_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for distractor (TrialHandler)
    distractor.addData('distractor_task_resp.keys',distractor_task_resp.keys)
    distractor.addData('distractor_task_resp.corr', distractor_task_resp.corr)
    if distractor_task_resp.keys != None:  # we had a response
        distractor.addData('distractor_task_resp.rt', distractor_task_resp.rt)
    distractor.addData('distractor_task_resp.started', distractor_task_resp.tStartRefresh)
    distractor.addData('distractor_task_resp.stopped', distractor_task_resp.tStopRefresh)
    distractor.addData('flicker.started', flicker.tStartRefresh)
    distractor.addData('flicker.stopped', flicker.tStopRefresh)
    thisExp.nextEntry()
    
# completed 30 repeats of 'distractor'


# ------Prepare to start Routine "pauseFMRI"-------
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
pauseFMRIComponents = [end_screen]
for thisComponent in pauseFMRIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
pauseFMRIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "pauseFMRI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = pauseFMRIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=pauseFMRIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_screen* updates
    if end_screen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_screen.frameNStart = frameN  # exact frame index
        end_screen.tStart = t  # local t and not account for scr refresh
        end_screen.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_screen, 'tStartRefresh')  # time at next scr refresh
        end_screen.setAutoDraw(True)
    if end_screen.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > end_screen.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            end_screen.tStop = t  # not accounting for scr refresh
            end_screen.frameNStop = frameN  # exact frame index
            win.timeOnFlip(end_screen, 'tStopRefresh')  # time at next scr refresh
            end_screen.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in pauseFMRIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "pauseFMRI"-------
for thisComponent in pauseFMRIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('end_screen.started', end_screen.tStartRefresh)
thisExp.addData('end_screen.stopped', end_screen.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
