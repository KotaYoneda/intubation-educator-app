tilt = 0
tone = 0
alerm_max = 0
beep_max = 0

def on_button_pressed_a():
    global tilt, tone, alerm_max, beep_max
    tilt = 0
    tone = 262
    alerm_max = 20
    beep_max = 20
    basic.show_string("Hello!")
    while False:
        basic.pause(100)
        if 0 >= alerm_max:
            music.play(music.string_playable("C5 A B G A F G E ", 120),
                music.PlaybackMode.UNTIL_DONE)
        else:
            if 0 >= beep_max:
                tone = input.acceleration(Dimension.X)
                music.play(music.tone_playable(tone, music.beat(BeatFraction.WHOLE)),
                    music.PlaybackMode.UNTIL_DONE)
            else:
                basic.show_icon(IconNames.HEART)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_forever():
    pass
basic.forever(on_forever)
