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
