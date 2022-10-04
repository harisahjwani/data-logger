def on_forever():
    basic.show_number(input.temperature())
    serial.write_value("CELCIUS", input.temperature())
basic.forever(on_forever)
