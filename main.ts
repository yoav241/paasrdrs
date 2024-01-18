music.play(music.stringPlayable("C D E F G A B C5 ", 120), music.PlaybackMode.UntilDone)
music.play(music.stringPlayable("C5 B A G F E D C ", 120), music.PlaybackMode.UntilDone)
radio.sendNumber(9)
radio.sendNumber(0)
radio.sendNumber(7)
control.inBackground(function () {
    control.reset()
})
