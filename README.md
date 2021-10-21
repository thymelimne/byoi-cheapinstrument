# byoi-cheapinstrument
Build-Your-Own-Instrument: an ancillary app to the CheapInstrument app.

Users are given the ability to hand-draw functions to define their own new musical instrument.

Ultimately, this is a drawing app that can output modules of data that you can go on to use in the CheapInstrument app, to make chords with your chosen sounds.

<h2>Music concepts</h2>
(At present understanding:) Within the realm of music synthesis, there are mathematical functions you can define to describe how an instrument sounds. This includes the "oscillator", also understandable as a waveform that effects the timbre of a musical instrument.

<br>Another such function is the "envelope", which is a measure of how loud the sound is over time. For example, when you play a note on a piano, there's the initial blast of sound that instantly begins to fade in loudness, and if you map this out on a graph it will look something like a downward logarithmic curve. Another slightly different example is a brass horn: There's an initial blast of loudness (air), which within a fraction of a second drops down to about half that initial loudness, and then it sustains at that approximate loudness until the horn player stops blowing that particular note. This layout of a note sound is referred to often, and is called Attack-Decay-Sustain-Release as a shorthand.

ADSR is roughly analogous to how most common real-world instruments produce sounds, and it's also simple and intuitive - there's no wacky Fourier transforms, or sine waves, or anything complex like you'd find with oscillators.[SEE2] For this reason, many synths throughout the past several decades have relied on the ADSR standard, some even giving their users four sliders to modulate the times of Attack, Decay, etc. to define the envelope function as essentially a series of four linear functions, for which you just tweak four parameters: the duration of each event in the ADSR envelope.

![image](https://user-images.githubusercontent.com/91765107/138204008-a2f45fa9-1cce-4a31-b63d-83716403153b.png)
<p align="center"><b>test</b></p>


With this project here, part of the goal is to break away from the convention of ADSR, and easily allow thinking-outside-the-box envelopes.


[SEE2]For more details on how diverse oscillators can get, and the different sounds you can get, here's a simple demonstration by the great Wendy Carlos. https://www.youtube.com/watch?v=4SBDH5uhs4Q
