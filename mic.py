# coding=utf-8
#測試音頻強度
import math
import pyaudio
import audioop

def audio_int(num_samples=50):   
    print "Getting intensity values from mic."
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=16000,
                    input=True,
                    frames_per_buffer=1024)

    values = [math.sqrt(abs(audioop.avg(stream.read(1024), 4))) 
              for x in range(num_samples)] 
    values = sorted(values, reverse=True)
    r = sum(values[:int(num_samples * 0.2)]) / int(num_samples * 0.2)
    print "Finished!"
    print "Average audio intensity is", r
    stream.close()
    p.terminate()
    return r
audio_int()