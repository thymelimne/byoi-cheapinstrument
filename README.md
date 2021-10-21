# byoi-cheapinstrument
Build-Your-Own-Instrument: an ancillary app to the CheapInstrument app.

Users are given the ability to hand-draw functions to <b>custom-define new musical instruments</b>.

Ultimately, this is a drawing app that can output modules of data that you can go on to use in the CheapInstrument app, to make chords with your chosen sounds.

<h2>Music concepts</h2>
(At present understanding:) Within the realm of music synthesis, there are mathematical functions you can define to describe how an instrument sounds. This includes the <b>"oscillator"</b>, also understandable as a waveform that effects the timbre of a musical instrument.

<br>Another such function is the <b>"envelope"</b>, which is a measure of how loud the sound is over time. For example, when you play a note on a piano, there's the initial blast of sound that instantly begins to fade in loudness, and if you map this out on a graph it will look something like a downward logarithmic curve. Another slightly different example is a brass horn: There's an initial blast of loudness (air), which within a fraction of a second drops down to about half that initial loudness, and then it sustains at that approximate loudness until the horn player stops blowing that particular note. This layout of a note sound is referred to often, and is called Attack-Decay-Sustain-Release as a shorthand.

<b>ADSR is roughly analogous to most common real-world instruments</b> in how they produce sounds, and it's also simple and intuitive - there's no wacky Fourier transforms, or sine waves, or anything complex like you'd often find with oscillators.[SEE2] For this reason, many synths throughout the past several decades have relied on the ADSR standard, some even giving their users four sliders to modulate the times of Attack, Decay, etc. to define the envelope function as essentially a series of four linear functions, for which you just tweak four parameters: the duration of each event in the ADSR envelope.

![image](https://user-images.githubusercontent.com/91765107/138204008-a2f45fa9-1cce-4a31-b63d-83716403153b.png)
```Above is a demonstration of the ADSR envelope standard.```


With this project here, part of the goal is to <b>break away</b> from the convention of ADSR, and easily allow thinking-outside-the-box envelopes. It was decided that, at least for the time being, <b>hand-drawing</b> is the simplest route to go to allow a user to define their own graphical function.

<h2>A drawing app</h2>

Using Python (in particular, an open-source Python library for graphics, called Kivy), an interactive drawing feature was made for this project. To make it user-friendly and intuitive, a fair amount of geometry has been put into the code, in hopes that the user's drawn line would look like a blotty-yet-smooth penstroke. Interestingly (well, mildly interesting), a small bug in the geometry has caused it to have a smooth ribbon-like quality, instead of what was intended. While this is okay for now, there is a plan to fix that bug, and enable the option to have a ribbon-stroke or a proper penstroke style for drawing.

![Screenshot (593)](https://user-images.githubusercontent.com/91765107/138289507-2b6e9fe8-9f8b-4e37-b775-5068084fb608.png)
```Above is an example of the app, drawn to resemble the ADSR standard.```

![Screenshot (594)](https://user-images.githubusercontent.com/91765107/138289599-72cc0bb6-3f61-43b5-887d-b969d7114d85.png)
```Above is a curve to vaguely evoke a piano note.```

![Screenshot (604)](https://user-images.githubusercontent.com/91765107/138289624-da71b222-05ec-4499-b279-7c17d9aa55ca.png)

![Screenshot (607)](https://user-images.githubusercontent.com/91765107/138289879-7e02b420-0edb-4077-ac08-6c662c578b52.png)

![Screenshot (608)](https://user-images.githubusercontent.com/91765107/138289909-51809ba4-9dbd-472c-bc4d-8d9ed939c3aa.png)
```Above are three more examples of possible functions.```

<h2>Upcoming challenge: data types</h2>
As said before, the point of this app is to output modules of data that can be used in the CheapInstrument music synthesizer application. However, it still needs to be figured out what this data should look like. More work needs to be done on the CheapInstrument app in order to decide how to internally represent an 'envelope' in its code, so that as many of the details drawn on a curve in this app can get expressed, but there isn't too much latency as the C.I. code would try to process a hundreds-long array of drawn points, to produce sound in real-time within one second...

<br>The solution might be a simple one, but some housekeeping is in order on the CheapInstrument app.</br>

<h2>Footnotes</h2>
[SEE2]For more details on how diverse oscillators can get, and the different sounds you can get, here's a simple demonstration by the great Wendy Carlos. https://www.youtube.com/watch?v=4SBDH5uhs4Q
