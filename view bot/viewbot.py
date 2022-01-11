import webbrowser
import time
import os

# asswhopper613 - asshole@34
# seedfaith87 - sexyboi69
# jseed1684 - legend@69


inpt = input("Enter youtube url: ")
inpt2 = input("Enter refresh rate(seconds): ")
inpt3 = input("Enter your default browser: ")
total = int(input('enter times to be viewed:'))
input2 = int(inpt2)

i=0


def OpenUrl():
    print("[+] %drd Viewed with"%i, input2, ' sec')
    os.system("TASKKILL /F /IM " + inpt3 + ".exe")
    webbrowser.open(inpt)
    time.sleep(int(input2))


while i<total:
    OpenUrl()
    i += 1
    time.sleep(int(input2))
    if input2 <= 45:
        if i % 5 == 0:
            input2 += 5
    else:
        print('Resetting to original .... ')
        a = int(inpt2)
        input2 = int(a)

# inpt2 = 20
# input2 = 50

