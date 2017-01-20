from gtts import gTTS
import pyglet
pyglet.lib.load_library('avbin')
pyglet.have_avbin=True
tts = gTTS(text='Hello World', lang='en')
tts.save("hello.mp3")
song = "hello.mp3"
sound_program = "C:\Program Files (x86)\K-Lite Codec Pack\MPC-HC64\mpc-hc64.exe"
music = pyglet.media.load(song)
music.play()
def exiter(dt):
    pyglet.app.exit()
print ("Song length is: %f", music.duration)
pyglet.clock.schedule_once(exiter, music.duration)
pyglet.app.run()


