from pydub import AudioSegment

name1 = "As The World Caves In - Matt Maltese (Cover by Sarah Cothran)"
name2 = "Ribs"

sound1 = AudioSegment.from_file(
    name1 + ".mp3", format="mp3")
sound2 = AudioSegment.from_file(
    name2 + ".mp3", format="mp3")


# 16000 ms crossfade == 16 seconds
combined = sound1.append(sound2, crossfade=16000)
combined.export("[Python] " + name1 + " + " + name2 + ".mp3", format="mp3")
