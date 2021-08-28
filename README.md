# music-blend-python

## Installation steps
* Use `git clone`.
* You need to install `pydub` using the command `npm install pydub`
* And also `FFMPEG` from [their official website.](https://ffmpeg.org/download.html) 
* Place inside the folder you cloned the repo 2 mp3 songs. 
* Open `script.py` and edit variables `name1` and `name2` with the names of the songs.
* OPTIONAL: Adjust the crossfade ms if you feel like it.
* Run it.
* You got a nice fade between 2 songs.

## Example
```
from pydub import AudioSegment

name1 = "Baby, You're a Rich Man"
name2 = "The Ultracheese"

sound1 = AudioSegment.from_file(
    name1 + ".mp3", format="mp3")
sound2 = AudioSegment.from_file(
    name2 + ".mp3", format="mp3")


# 16000 ms crossfade == 16 seconds
combined = sound1.append(sound2, crossfade=16000)
combined.export("[Python] " + name1 + " + " + name2 + ".mp3", format="mp3
```

