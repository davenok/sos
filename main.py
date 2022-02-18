# I wrote this for some reason...
# Trying to get rid of Alpaca King

from utime import sleep_ms
import machine
import time

led = machine.Pin(25, machine.Pin.OUT)

def the_led(length):
    led.value(1)
    time.sleep_ms(length)
    led.value(0)
    time.sleep_ms(int(length))

def SendLetter(letter):
    MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', '1':'.----', '2':'..---', 
                    '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', 
                    '8':'---..', '9':'----.', '0':'-----', ',':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-', '(':'-.--.', ')':'-.--.-',
                    '\'':'.----.','!':"-.-.--"}
    the_letter = MORSE_CODE_DICT[letter]
    print("Letter Received: " + letter + the_letter)

    for sound in the_letter:
        print(sound)
        if sound == ".":
            length = 150
            the_led(int(length))
        else:
            length = 450
            the_led(int(length))
    sleep_ms(125)

while True:
    print("Hey, got a message for you")
    message = "SOS"
    for l in message.upper():
        if l == " ":
            time.sleep_ms(1500)
        else:
            SendLetter(l)
        time.sleep_ms(100)
    print("message end")
    time.sleep(5)

print("end")