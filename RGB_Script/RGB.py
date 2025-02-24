from gpiozero import PWMLED
from tkinter import TK, Scale, HORIZONTAL

red = PWMLED(17)
blue = PWMLED(22)
green = PWMLED(27)

def update_red(val):
    red.value = int(val)/100.00
def update_green (val):
    green.value = int(val)/100.00
def update_blue(val):
    blue.value = int(val) / 100.00

root = Tk()
root.title("RGB")

redslider = Scale(root, from_=0, to=100, orient=HORIZONTAL, label="Red", command=update_red)
redslider.pack()
greenslider = Scale(root, from_=0, to=100, orient=HORIZONTAL, label="Green", command=update_green)
greenslider.pack()
blueslider = Scale(root, from_=0, to=100, orient=HORIZONTAL, label="Blue", command=update_blue)
blueslider.pack()

root.mainloop()