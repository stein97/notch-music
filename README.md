# notch-music
Notched sound therapy works by cutting a band around your tinnitus pitch out of the music. The common research approach removes a one-octave band centered on your tinnitus frequency.

At 4 kHz that’s roughly 2.8–5.7 kHz, not just 4 kHz exactly.

Go to https://audionotch.com/ and determine Your Tinnitus Profile

install ffmpeg

Move the MP3 into their own folder and run the following script.

for f in *.mp3; do ffmpeg -i "$f" -af "bandreject=f=4000:width_type=o:w=1,bandreject=f=4000:width_type=o:w=1" -q:a 2 "notched_$f"; done

