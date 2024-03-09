let tilt = 0
let tone = 0
let alerm_max = 0
let beep_max = 0
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    tilt = 0
    tone = 262
    alerm_max = 20
    beep_max = 20
    basic.showString("Hello!")
    while (false) {
        basic.pause(100)
        if (0 >= alerm_max) {
            music.play(music.stringPlayable("C5 A B G A F G E ", 120), music.PlaybackMode.UntilDone)
        } else if (0 >= beep_max) {
            tone = input.acceleration(Dimension.X)
            music.play(music.tonePlayable(tone, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
        } else {
            basic.showIcon(IconNames.Heart)
        }
        
    }
})
basic.forever(function on_forever() {
    
})
