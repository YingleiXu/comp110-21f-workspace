"""Repeating a beat in a loop."""

__author__ = "730529273"
i: int = 0
repeat_beat: str = input("What beat do you want to repeat? ")
repeated_times: int = int(input("How many times do you want to repeat it? "))
beat: str = ""
if repeated_times <= i:
    print("No beat...")

while i < repeated_times:
  
    if i < repeated_times - 1:
        beat = beat + repeat_beat + " "
    else:
        beat = beat + repeat_beat
    i = i + 1
print(beat)