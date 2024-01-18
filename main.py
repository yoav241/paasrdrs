music.play(music.string_playable("C D E F G A B C5 ", 120),
    music.PlaybackMode.UNTIL_DONE)
music.play(music.string_playable("C5 B A G F E D C ", 120),
    music.PlaybackMode.UNTIL_DONE)
radio.send_number(9)
radio.send_number(0)
radio.send_number(7)

def on_in_background():
    control.reset()
control.in_background(on_in_background)
