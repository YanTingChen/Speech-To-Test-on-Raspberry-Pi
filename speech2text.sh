#!/bin/bash
echo "Recording...Press Ctrl+C to stop."

arecord -D "plughw:1,0" -q -f cd -t wav | ffmpeg -loglevel panic -y -i - -ar 16000 -acodec flac file.flac > /dev/null 2>&1

echo "Processing....."
wget -4 -q -U "Mozilla/5.0" --post-file file.flac --header "Content-Type:audio/x-flac; rate=16000" -O - "http://www.google.com/intl/en/chrome/demos/speech.html" | cut -d\" -f12 >stt.txt

echo -n "You said:"
cat stt.txt
rm file.flac > /dev/null 2>&1
