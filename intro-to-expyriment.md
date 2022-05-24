% Introduction to Expyriment
% Christophe@pallier.org
% May 2022

# Why Expyriment?

Some psychology experiment generators:

* [Psychtoolbox](http://psychtoolbox.org) (MATLAB/Octave). 
   
* [Psychopy](https://www.psychopy.org)  (either a Python library, or self-contained with a Builder "à la" Eprime))

* [Expyriment](https://www.expyriment.org) (a Python library). 


Pros:

- Expyriment is cleaner and simpler than the other two (in my opinion). It promotes good programming practices (readability!).

- It is good enough for most experiments (so far, the only tasks I ould not program involved the presentation of two simultaneous videos).

- The timing is ok when programmed correctly (VSYNC blocking,... See Retinotopy demo). For time critical applications, one must check timings as this is hardware/driver dependent. 

Cons:

* As it relies on Python, it is not possible to run remote on-line experiments.

* Small user community => lack of documentation and examples on the web (yet the API is very well-documented (see  <https://docs.expyriment.org/expyriment.html>)).

* Dependency on the Python module `pygame 1.9.6` can cause problems during the installation.


# Requirements for this tutorial

* A Python environment (e.g. Anaconda Python 3)

* The expyriment module (check installation instructions at <https://docs.expyriment.org/Installation.html>)

* A local copy of <https://github.com/chrplr/tutorial-expyriment.git> (you can clone it with git, or download the zip file)

# First example

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

Execute this code (You will need to press the space bar to end it)


# Stimuli

* `experiment.stimuli` provides basic stimuli (circle, polygon, cross, text, sound, image...). See <https://docs.expyriment.org/expyriment.stimuli.html>

* `expyriment.stimuli.extras` provides more advanced stimuli like Gabor pattern, DotCloud, ...


# simple detection of visual events

1. Download [simple-detection-visual-expyriment.py](examples/simple_reaction_times/simple-detection-visual-expyriment.py)

2. Run it, then check the results in the subfolder `data`. Note that one csv file pe subject is generated.

3. Have a look at the source code.

# simple detection of audio events

1. Download [simple-detection-audio-expyriment.py](examples/simple_reaction_times/simple-detection-audio-expyriment.py), as well as the 

2. Run it.

3. Compare it with the visual version.


# simple decision (parity task)

* Run [parity.py](examples/parity_decision/parity.py)

* Run [parity_feedback.py](examples/parity_decision/parity_feedback.py)

* See also [parity_short.py](examples/parity_short/really_short_exp.py)


# Simple decisions (left vs. right)

[left_right_detection.py](examples/left_right_detection_task/left_right_detection.py)

# `Trial` and `Block` objects

The `design` submodule of expyriment provides `Trial` and `Block` objects to structure the experiment (Note that these objects are in no way necessary to present stimuli.)



* [grey-levels.py](examples/simple_reaction_times/grey-levels.py) illustrates the use of `set_factor()` and `get_factor()` for trials.

* [left_right_center_detection.py](examples/left_right_detection_task/left_right_center_detection.py)
q
* [simple-detection-audiovisual.py](examples/simple_reaction_times/simple-detection-audiovisual.py)

# More complex examples:

* Posner ANT task: <examples/Posner_attention_networks_task>

* Lexical Decision task: <examples/lexical_decision/lexdec_v3.py>

* Mental Logic Task: <examples/mental_logic_card_game/>

