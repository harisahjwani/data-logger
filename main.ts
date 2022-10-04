basic.forever(function on_forever() {
    basic.showNumber(input.temperature())
    serial.writeValue("CELCIUS", input.temperature())
})
