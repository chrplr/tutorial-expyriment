% Introduction to Expyriment
% Christophe@pallier.org
% May 2022

# Expyriment?

Some psychology experiment generators:

* [Psychtoolbox](http://psychtoolbox.org) (MATLAB/Octave). 
   
* [Psychopy](https://www.psychopy.org)  (either a Python library, or self-contained with a Builder "à la" Eprime)

* [Expyriment](https://www.expyriment.org) (a Python library). 


Pros:

- Expyriment is cleaner and simpler than the previous two (in _my_ opinion). It promotes good programming practices (readbility!).

- It is good enough for most experiments (the only limitation I encountered so far was that I coulkd not presente simultaneaously 2 videos).

- The timing is fine if you use it correctly (setting blocking to VSYNC, etc.). As always, for time critical application, one must check the timings with external equipement as this is hardware/driver depedent.

=> Show the Retinotopy demo.

Cons:

* Small user community => lack of documentation and examples on the web (yet the - the API is very well-documented (see  <https://docs.expyriment.org/expyriment.html>)).

* Dependency on the old Python module `pygame 1.9.6` which can cause problems during the installation.



# Examples of scripts on the Net

As the community is very small, there are very few tutorials and examples on the Net. Yet:

1. <https://docs.expyriment.org/old/0.8.0/Examples.html> (sources at <https://github.com/expyriment/expyriment-stash/tree/master/examples/behavioural>)

2. <https://mbroedl.github.io/cognitive-tasks-for-expyriment/>

3. <https://github.com/chrplr/PCBS/tree/master/experiments>  (used in my lectures <https://pcbs.readthedocs.io/en/latest/running-experiments.html>)





# Stimuli

Guess what the following piece of code does:

```
from expyriment import stimuli

fixation = stimuli.FixCross()
picture = stimuli.Picture("cat.png")
sound = stimuli.Audio("sentence.wav")

fixation.present()
exp.clock.wait(1000)
picture.present()
sound.present()

key, rt = exp.keyboard.wait_char()
```


* `experiment.stimuli` provides basic stimuli (circle, polygon, cross, text, sound, image...). See <https://docs.expyriment.org/expyriment.stimuli.html>

* `expyriment.stimuli.extras` provides more advanced stimuli, e.g. Gabor pattern, DotCloud, etc.


# Minimal skeleton for an expyriment script 

To make the preceding code actually work, you need a bit of boilerplate (See <https://docs.expyriment.org/Tutorial.html>)

```
from expyriment import design, control, stimuli

exp = design.Experiment(name="Experiment")

control.initialize(exp)

fixation = stimuli.FixCross()
picture = stimuli.Picture("cat.png")
sound = stimuli.Audio("sentence.wav")

control.start()

fixation.present()
exp.clock.wait(1000)
picture.present()
sound.present()
key, rt = exp.keyboard.wait_char(' ')

control.end()
```

Execute this script (You will need to press the space bar to end it)


# simple detection of visual events


1. Download [simple-detection-visual-expyriment.py](https://github.com/chrplr/PCBS/blob/master/experiments/xpy_simple_reaction_times/simple-detection-visual-expyriment.py)

2. Run it, than check the results in the subfolder `data`

3. Let's have a look at it.

# simple detection of audio events

1. Download [simple-detection-audio-expyriment.py](https://github.com/chrplr/PCBS/blob/master/experiments/xpy_simple_reaction_times/simple-detection-audio-expyriment.py), as well as the 

2. Run it.

3. Compare it with the visual version.


# simple decision (parity task)

* Run [parity.py](https://github.com/chrplr/PCBS/blob/master/experiments/xpy_parity_decision/parity.py)

* Run [parity_feedback.py](https://github.com/chrplr/PCBS/blob/master/experiments/xpy_parity_decision/parity_feedback.py)


# Simple decisions (left vs right)

[left_right_detection.py](https://github.com/chrplr/PCBS/blob/master/experiments/xpy_left_right_detection_task/left_right_detection.py)

# Introducing `Trial` and `Block` objects

The `design` submodule of expyriment provides `Trial` and `Block` objects to structe and exepriment. (Note that these objects are not necessary to present stimuli.)

* [grey-levels.py](https://github.com/chrplr/PCBS/blob/master/experiments/xpy_simple_reaction_times/grey-levels.py)

* [left_right_center_detection.py](https://github.com/chrplr/PCBS/blob/master/experiments/xpy_left_right_detection_task/left_right_center_detection.py)

* [simple-detection-audiovisual.py](https://github.com/chrplr/PCBS/blob/master/experiments/xpy_simple_reaction_times/simple-detection-audiovisual.py)

# More complex examples:


* Posner ANT task: <https://github.com/chrplr/PCBS/tree/master/experiments/xpy_Posner_attention_networks_task>

* Lexical Decision tasl: <>

* Mental Logic Task: <>

