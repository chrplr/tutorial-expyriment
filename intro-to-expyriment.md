% Introduction to Expyriment
% Christophe@pallier.org
% May 2022

# Requirements for this tutorial

1. A Python environment

   E.g., [Anaconda Python 3](https://www.anaconda.com/products/distribution).

2. The [expyriment module](https://www.expyriment.org) 

   Check installation instructions at <https://docs.expyriment.org/Installation.html>).

3. A local copy of <https://github.com/chrplr/tutorial-expyriment.git>, which can obtain by by downloading this [zip file](https://github.com/chrplr/tutorial-expyriment/archive/refs/heads/main.zip) or with git:

         git clone https://github.com/chrplr/tutorial-expyriment
	  


Note: This tutorial assumes that you know how to execute Python code from a command line in a terminal window (if you don't, see, e.g., <https://www.youtube.com/watch?v=2yhcWvBt7ZE>).



# First example

Guess what the following piece of code is meant to do:

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

Execute this code in `ipython` (or with `python example_01.py`) 

Note: You will need to press the space bar to quit it.


# Stimuli

* `experiment.stimuli` provides basic stimuli (circle, polygon, cross, text, sound, image...). See <https://docs.expyriment.org/expyriment.stimuli.html>

* `expyriment.stimuli.extras` provides more advanced stimuli like Gabor pattern, DotCloud, (you need to )...


# simple detection of visual events

1. Download [simple-detection-visual-expyriment.py](examples/simple_reaction_times/simple-detection-visual-expyriment.py)

2. Run it, then check the results in the subfolder `data`. Note that:

  * there is one `.xpd` file per subject (the subject's number is automatically incremented each time you launch the expyriment script).
  * this `.xpd` file is actually a comma-separated-values (csv) file, with additionnal information in lines starting with `#`.

    You can import this file data in Python into a pandas dataframe using:

           pandas.read_csv('filename.xpd', comment='#')

    or in R:
   
		   read.csv('filename.xpd', comment.char = '#')

3. Have a look at the source code.

   Its core consists of:

           target = stimuli.FixCross(size=(50, 50), line_width=4)
           blankscreen = stimuli.BlankScreen()

		   for i_trial in range(N_TRIALS):
			   blankscreen.present()
			   waiting_time = random.randint(MIN_WAIT_TIME, MAX_WAIT_TIME)
			   exp.clock.wait(waiting_time)
			   target.present()
			   key, rt = exp.keyboard.wait(duration=MAX_RESPONSE_DELAY)
			   exp.data.add([i_trial, waiting_time, key, rt])

# Simple detection of audio events

1. Download [simple-detection-audio-expyriment.py](examples/simple_reaction_times/simple-detection-audio-expyriment.py), as well as the 

2. Run it.

3. Compare its source code with the one of the visual version, for example with:

        meld simple-detection-visual-expyriment.py simple-detection-audio-expyriment.py

   The only essential difference is the line:

        target = stimuli.FixCross(size=(50, 50), line_width=4)
		
   which was changed into:

	    target = stimuli.Audio('click.wav')

   The code in the main loop remains the same!

# Simple decision (parity task)


Let' now see the case where the participant must take a decision at each trial and press one of two keys. 

In [parity.py](examples/parity_decision/parity.py), the participant must determine the parity of a single digit number.

[parity_feedback.py](examples/parity_decision/parity_feedback.py)
adds auditory feedback when the response is wrong.


Note: See also [parity_short.py](examples/parity_short/really_short_exp.py), a very short example from expyriment's documentation.


# Simple decisions (left vs. right)


[left_right_detection.py](examples/left_right_detection_task/left_right_detection.py) is a similar example as parity.

# `Trial` and `Block`

The `design` submodule of expyriment provides `Trial` and `Block` objects to structure the experiment. 

* [grey-levels.py](examples/simple_reaction_times/grey-levels.py) illustrates the use of `set_factor()` and `get_factor()` for trials.

* [left_right_center_detection.py](examples/left_right_detection_task/left_right_center_detection.py)
q
* [simple-detection-audiovisual.py](examples/simple_reaction_times/simple-detection-audiovisual.py)

(Remark that these objects are in no way necessary to present stimuli! You can program without them if its makes the code more readable)

# More complex examples:

* [Posner ANT task](examples/Posner_attention_networks_task)

        cd examples/Posner_attention_networks_task
		python posner_task.py

* [Lexical Decision task](examples/lexical_decision/) 

        cd examples/lexical_decision
	    python lexdec_v3.py stimuli.csv

* [Mental Logic Task](examples/mental_logic_card_game/): illustrates the use of `stimuli.Canvas` to present several pictures simultaneaously)

		cd examples/mental_logic_card_game/
		python mental_logic_card_game.py

* [Audiovis](https://github.com/chrplr/audiovis): a general audio-visual stimuli presentation script.


# Timing

* Run:

		cd examples/tearing_test
		python tearing-test.py
  
  If the vertical bar appears broken or moves very fast, this means that the `present()` function is not blocking on (waiting for) vertical retrace. 

  You may need to set up you video card to block on “vsync”. 
  
  Under Linux, if you have a nVidia GPU, you need to run `nvidia-settings`. If you have an AMD GPU:
  

		sudo apt install xvattr
		echo "export vblank_mode=3" > /etc/profile.d/radeon.sh

  See the documentation of the `expyriment.control.default.open_gl` at <https://docs.expyriment.org/expyriment.control.defaults.html> 

* Read https://docs.expyriment.org/Timing.html

* We also provide a script to check duration of presetentation of a visual stimulus with a photodiode, and its synchrony with a sound:

        cd examples/check-audio-visual-timing
		python check-audio-visual-timing.py


# Conclusion

### Pros:

- Expyriment is a clean and simple psychology experiment generator. It promotes good programming practices (readability!).

- It is good enough for most experiments (so far, the only task I could not program involved the presentation of two simultaneous videos).

- The timing is fine when programmed correctly (VSYNC blocking,... See Retinotopy demo). For time critical applications, one must check timings as this is hardware/driver dependent. 

### Cons:

* As it relies on Python, it is not possible to run remote on-line experiments.

* Small user community => lack of documentation and examples on the web (yet the [interface](https://docs.expyriment.org/expyriment.html) is very well-documented.

* Dependency on the Python module `pygame 1.9.6` can cause problems during the installation. 


# Other ressources 

   *  <https://github.com/expyriment/expyriment-stash>

   *  <https://mbroedl.github.io/cognitive-tasks-for-expyriment/>

