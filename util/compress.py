import subprocess

def compressAudio():
    subprocess.call(['ffmpeg', '-i', '../audio/test.mp3', '-acodec', 'pcm_s16le','-ar','8000','-ac','1','./audio/test.wav'])
    subprocess.call(['ffmpeg', '-i', '../audio/test.wav', '-b:a', '16k', './audio/test2.wav'])